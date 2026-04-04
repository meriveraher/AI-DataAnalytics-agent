import gradio as gr
import matplotlib.pyplot as plt

# 1. PRE-PROCESS: Run cleaning tools ONCE before launching the UI
print("Cleaning data...")
df_cleaned = df.copy()
standardize_student_levels(df_cleaned)
validate_session_metrics(df_cleaned)
sanitize_ratings(df_cleaned)

# 2. THE MASTER LOGIC FUNCTION
#Agent's thinking structure
from pydantic import BaseModel, Field
from typing import Literal, Optional


class AgentDecision(BaseModel):
    tool_name: Literal["clean", "stats", "plot", "report"] = Field(description="The tool to use")
    column_name: str = Field(description="The numeric column to analyze")
    group_by_column: Optional[str] = Field(None, description="The category to group by (e.g., 'StudentLevel') if comparing groups")
    justification: str = Field(description="Why this tool and grouping was chosen")

# Initializing the memory list
history_buffer = []


def master_agent_interface(query):
    global history_buffer
    plt.close('all')
    
    # Step 1. Ask the LLM to decide what to do
    past_context = "\n\n".join(history_buffer)
    system_context = f"""
    You are a Data Science Router. 
    Columns available: {df_cleaned.columns.tolist()}
    
    RULES:
    1. If the user asks to 'compare' or asks 'which level/group', you MUST set group_by_column to 'StudentLevel'.
    2. 'TotalPrompts' and 'SatisfactionRating' are numeric. 'StudentLevel' is categorical.

    
    RECENT MEMORY (Previous 4 findings):
    {past_context if past_context else "No previous history."}
    
    User Query: {query}
    """
    
    # Using existing generate function with the Pydantic model
    decision = generate(system_context, response_format=AgentDecision, model="gpt-4o-mini")
    
    # Step 2. Execute the tool based on the LLM's decision
    fig = None
    conclusion = ""
    stats_output = ""
    
    if decision.tool_name == "plot":
        # The LLM picked 'plot' and identified the column!
        fig = plot_bar_chart_plt(df_cleaned, x_col='studentlevel', y_col=decision.column_name)
        stats_output = calculate_column_stats(
            df_cleaned, 
            column=decision.column_name, 
            group_by=decision.group_by_column
        )
        conclusion = f"### Statistics for {decision.column_name} (Grouped by {decision.group_by_column})\n{stats_output}"

    elif decision.tool_name == "stats":
        stats_output = calculate_column_stats(
            df_cleaned, 
            column=decision.column_name, 
            group_by=decision.group_by_column
        )
        conclusion = f"### Statistics for {decision.column_name} (Grouped by {decision.group_by_column})\n{stats_output}"

    elif decision.tool_name == "report":
        conclusion = generate_summary_report(df_cleaned, {}, query)
        
    
    # Step 3. Ask the LLM to summarize findings
    summary_prompt = f"""
    The user asked: {query}
    Here are the results of the data analysis:
    {stats_output}
    
    Provide a brief, 2-sentence executive summary. 
    Format it exactly like this: 
    "The level with the highest {decision.column_name} is [Level] because [Observation from data]."
    """
    
    ai_summary = generate(summary_prompt, model="gpt-4o-mini")
    
    # 4. Combine everything for the UI
    final_output = f"### 📊 Analysis Findings\n\n{stats_output}\n\n**Conclusion:** {ai_summary}"
    
    # Safety: ensure a figure exists for Gradio
    if fig is None:
        fig = plt.figure(figsize=(1,1))
        #plt.axis('off')
    #Add newest result to memory
    history_buffer.append(f"**Q:** {query} | **A:** {ai_summary}")
    if len(history_buffer) > 4:
        history_buffer.pop(0)
    # Create a formatted string to show in the UI
    history_md = "### 📜 Recent History\n" + "\n\n".join(history_buffer)

        
    return fig, final_output, history_md

# 3. GRADIO LAYOUT
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Data Analytics AI Agent 🤖 ")
    
    with gr.Tab("Analysis Dashboard"):
        with gr.Row():
            with gr.Column(scale=1):
                user_input = gr.Textbox(label="Ask your Agent", placeholder="e.g., Show me a plot of prompts by level")
                submit_btn = gr.Button("Execute", variant="primary")
                history_display = gr.Markdown("History will appear here after the first query.")
            
            with gr.Column(scale=2):
                plot_output = gr.Plot(label="Visualization Tool Output")
                text_output = gr.Markdown(label="Agent Analysis")

    with gr.Tab("Data Health"):
        gr.Markdown("### Current Cleaned Data Preview")
        gr.Dataframe(df_cleaned.head(10))

    submit_btn.click(
        fn=master_agent_interface, 
        inputs=user_input, 
        outputs=[plot_output, text_output, history_display]
    )

demo.launch(share=True, inline=False)
