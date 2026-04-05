
try:
    df = pd.read_csv("ai_assistant_usage_student_life.csv")
    print("File loaded successfully!")
    df.columns = df.columns.str.replace(' ', '_').str.replace('.', '').str.lower()
    print(f"✅ Loaded {len(df)} Dataset with {len(df.columns)} columns")
    print(df.head(5))
except FileNotFoundError:
    print("The system can't find the file.")
