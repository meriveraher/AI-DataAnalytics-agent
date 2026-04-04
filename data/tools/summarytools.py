#CONCLUSION AND SUMMARY TOOLS

def generate_summary_report(df: pd.DataFrame, stats_results: dict, insight_goal: str):
    """
    Combines raw data stats with a high-level goal to produce a 
    structured report. This tool helps the agent 'focus' its conclusion.
    """
    report_template = f"""
    --- DATA ANALYTICS REPORT ---
    GOAL: {insight_goal}
    TOTAL SESSIONS ANALYZED: {len(df)}
    
    KEY METRICS:
    {stats_results}
    
    CRITICAL FINDINGS:
    - The average AI usage per session is {df['sessionlengthmin'].mean():.2f} minutes.
    - Highest adoption is seen in the {df['studentlevel'].mode()[0]} demographic.
    - User satisfaction correlates with {df[['satisfactionrating', 'totalprompts']].corr().iloc[0,1]:.2f} prompt frequency.
    """
    return report_template

def recommend_actions(df: pd.DataFrame):
    """
    Uses data thresholds to trigger specific recommendations.
    This moves the agent from 'What happened' to 'What should we do'.
    """
    recommendations = []
    
    # Logic-based recommendations
    avg_satisfaction = df['satisfactionrating'].mean()
    if avg_satisfaction < 3.5:
        recommendations.append("LOW SATISFACTION: Investigate 'TaskType' to see where AI is failing students.")
    
    undergrad_usage = df[df['studentlevel'] == 'Undergraduate']['totalprompts'].mean()
    grad_usage = df[df['studentlevel'] == 'graduate']['totalprompts'].mean()
    
    if grad_usage > undergrad_usage * 1.5:
        recommendations.append("ADOPTION GAP: Undergraduates are using AI significantly less than Graduates. Consider introductory workshops.")

    return recommendations if recommendations else ["Data looks stable. Maintain current support levels."]
    
