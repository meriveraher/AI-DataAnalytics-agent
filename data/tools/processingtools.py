
def calculate_column_stats(df: pd.DataFrame, column: str, group_by: str = None):
    """
    Calculates statistics and returns a formatted Markdown table for Gradio.
    """
    # 1. Validation
    if column not in df.columns:
        return f"⚠️ Error: Column '{column}' not found."
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return f"⚠️ Error: '{column}' is not numeric and cannot be aggregated."

    stats_list = ['mean', 'median', 'max', 'min', 'count', 'std']

    if group_by and group_by in df.columns:
        # 2. Perform grouped aggregation
        report = df.groupby(group_by)[column].agg(stats_list).round(2)
        # 3. Use .to_markdown() for beautiful Gradio tables
        return report.to_markdown()
    else:
        # 4. Perform global aggregation
        report = df[column].agg(stats_list).round(2)
        # Convert Series to DataFrame so it renders as a table
        return report.to_frame().T.to_markdown(index=False)
        
def check_correlation(df: pd.DataFrame, col1: str, col2: str):
    """Calculates the Pearson correlation between two numeric columns."""
    correlation = df[col1].corr(df[col2])
    
    if correlation > 0.7:
        strength = "strong positive"
    elif correlation < -0.7:
        strength = "strong negative"
    else:
        strength = "weak"
        
    return f"The correlation between {col1} and {col2} is {correlation:.2f}, which is a {strength} relationship."
