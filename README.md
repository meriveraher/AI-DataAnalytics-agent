# **🤖 Data Analytics AI Agent 🤖** 

This AI-powered Analytics Agent, will have for goal investigate how AI assistants such as ChatGPT are used by students at different academic levels use AI tools like ChatGPT for tasks such as coding, writing, studying, and brainstorming. Designed for learning, EDA, and ML experimentation.

# This AI Agent is able to:

1. **🧹 Clean:** Agent will clean messy data, handle missing values, and structure the datasets for analysis.
2. **🔢 Process/Analyze:** Users can ask questions in plain English (e.g., "What was the average number of students using AI assistants?") and agent will be able to produce an answer to the query.
3. **📊 Visualize:** Agent can automatically create charts, graphs, to illustrate data trend.
4. **📋 Provide a conclusion:** Agent will summarize findings, create reports, and recommend actions.


# The logic behind every query

- **The Data Foundation:** Agent will automatically clean and fix student levels and ratings.
- **The Toolset:** Agent will decide which Python function to use for statistics and Matplotlib visualizations.
- **The Brain:** A structured LLM router using the custom generate function.
- **The Memory:** Agent will keep memory of last four queries to keep the conversation coherent.
- **The UI:** A professional Gradio interface with Markdown tables and live charts.


<img width="639" height="309" alt="Screenshot 2026-04-01 at 3 44 35 PM" src="https://github.com/user-attachments/assets/d43bcf0d-8d56-4b10-8b3b-37f6c2dcd304" />


# **How to use this agent**

**Prerequisites**

- OpenAI API
- Basic familiarity with Python and pandas


**1. Clone the repo**

git clone https://github.com/meriveraher/AI-DataAnalytics-agent.git
cd AI-DataAnalytics-agent


**2. Install dependencies ans import libraries**

library imports/imports.py


**3. Install Dataset**

data/ai_assistant_usage_student_life.csv
data/loadingdataset.py


# About the Dataset 🗄️

**AI Assistant Usage in Student Life**

This dataset from Kaggle simulates 10,000 sessions of students interacting with an AI assistant (like ChatGPT or similar tools) for various academic tasks. Each row represents a single session, capturing the student’s level, discipline, type of task, session length, AI effectiveness, satisfaction rating, and whether they reused the AI tool later.

Link to download:
https://www.kaggle.com/datasets/ayeshasal89/ai-assistant-usage-in-student-life-synthetic?resource=download


Variables
- SessionID--Unique session identifier
- StudentLevel--Academic level: High School, Undergraduate, Graduate
- Discipline--Student’s field of study (e.g., CS, Psychology, etc.)
- SessionDate--Date of the session
- SessionLengthMin--Length of AI interaction in minutes
- TotalPrompts--Number of prompts/messages used
- TaskType--Nature of the task (e.g., Coding, Writing, Research)
- AI_AssistanceLevel--1–5 scale on how helpful the AI was perceived to be
- FinalOutcome--What the student achieved: Assignment Completed, Idea Drafted, etc.
- UsedAgain--Whether the student returned to use the assistant again
- SatisfactionRating--1–5 rating of overall satisfaction with the session


**4. Run the tools**

tools/cleaningtools.py
tools/processingtools.py
tools/summarytools.py
tools/visualizingtools.py

**5. Run the demo**

demo/thedemo.py

The demo file includes:
1. PRE-PROCESS: Run cleaning tools ONCE before launching the UI
2. THE MASTER LOGIC FUNCTION, the agent's thinking structure
   class AgentDecision(BaseModel)
    #Initializing the memory list
    history_buffer = []
    def master_agent_interface(query)
    def master_agent_interface(query)
3. GRADIO LAYOUT
When running this, you will get a link to the gradio demo, it lasts 72 hours.


**If you would like to skip all the previous steps, make a copy of the Jupyter notebook, everything is packed there!

Thank you for visisting my repo! 

-Maria Rivera :)
