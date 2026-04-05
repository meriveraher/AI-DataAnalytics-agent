#Cleaning tools


from difflib import get_close_matches

# Tool 1: Academic Level Standardizer
def standardize_student_levels(df: pd.DataFrame):
    """
    Ensures StudentLevel is strictly: 'High School', 'Undergraduate', or 'Graduate'.
    Fixes common synthetic issues like 'undergrad' or 'highschool'.
    """
    valid_levels = ['High School', 'Undergraduate', 'Graduate']
    column = 'studentlevel'
    
    def match_level(val):
        if pd.isna(val): return val
        matches = get_close_matches(val.title(), valid_levels, n=1, cutoff=0.6)
        return matches[0] if matches else "Other"

    df[column] = df[column].apply(match_level)
    return f"Standardized {column} to primary academic tiers."

# Tool 2: Session Logic Validator
def validate_session_metrics(df: pd.DataFrame):
    """
    Identifies 'Impossible Sessions'. 
    Example: TotalPrompts > 0 but SessionLengthMin is 0, or vice versa.
    """
    # Flagging rows where AI was used but no time was recorded
    mask = (df['totalprompts'] > 0) & (df['sessionlengthmin'] <= 0)
    invalid_count = mask.sum()
    
    # Impute 1 minute for sessions with prompts but 0 time
    df.loc[mask, 'sessionlengthmin'] = 1
    
    return f"Fixed {invalid_count} sessions with prompts but zero duration."

# Tool 3: Discipline Grouper
def group_disciplines(df: pd.DataFrame, top_n: int = 10):
    """
    In this dataset, 'Discipline' can be very fragmented (e.g., 'CS', 'CompSci').
    This tool groups infrequent disciplines into 'Other' to prevent overfitting.
    """
    counts = df['discipline'].value_counts()
    keep = counts.nlargest(top_n).index
    df['discipline'] = df['discipline'].where(df['discipline'].isin(keep), 'Other')
    
    return f"Consolidated disciplines. Top {top_n} retained, others moved to 'Other'."

# Tool 4: Satisfaction Rating Clipper
def sanitize_ratings(df: pd.DataFrame):
    """
    SatisfactionRating and AI_AssistanceLevel should be 1-5.
    This tool clips any synthetic noise outside this range.
    """
    for col in ['satisfactionrating', 'ai_assistancelevel']:
        df[col] = df[col].clip(1, 5).round(0).astype(int)
        
    return "Clipped and rounded ratings to strict 1-5 integer scale."


"""
"Check for Fairness" Tool
As this is educational data, the agent should also check for class imbalance. If "Graduate" students only make up 
1% of your data, the agent's analytics will be biased toward "Undergraduates."
"""
def check_representation(df: pd.DataFrame, column: str = 'studentlevel'):
    """Reports the percentage distribution of a category to alert for bias."""
    distribution = df[column].value_counts(normalize=True) * 100
    report = distribution.to_dict()
    return f"Representation Check for {column}: {report}"
