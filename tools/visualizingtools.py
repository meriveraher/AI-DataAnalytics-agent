#VISUALIZING TOOLS

import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean visual style for all plots
sns.set_theme(style="whitegrid")

def plot_histogram_plt(df: pd.DataFrame, column: str):
    """Shows the distribution/frequency of a numeric column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, color='skyblue')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('frequency')
    plt.show()
    return f"Histogram of {column} rendered."

def plot_bar_chart_plt(df: pd.DataFrame, x_col: str, y_col: str, operation: str = "mean"):
    """Compares a metric (y) across categories (x)."""
    fig = plt.figure(figsize=(10, 6))
    
    # Seaborn's barplot can handle the 'mean' calculation automatically
    # 'estimator' can be np.mean, np.median, np.sum, or len (for count)
    import numpy as np
    estimator_map = {"mean": np.mean, "median": np.median, "sum": np.sum, "count": len}
    
    sns.barplot(
    data=df, 
    x=x_col, 
    y=y_col, 
    estimator=estimator_map.get(operation, np.mean), 
    hue=x_col,      
    legend=False,   
    palette="viridis"
)
    plt.title(f'{operation.title()} {y_col} by {x_col}')
    plt.xticks(rotation=45)
    
    return fig

def plot_scatter_plt(df: pd.DataFrame, x_col: str, y_col: str, color_by: str = None):
    """Shows the relationship between two numbers."""
    fig = plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=color_by, palette="magma", alpha=0.7)
    
    # Add a trend line for better analysis
    sns.regplot(data=df, x=x_col, y=y_col, scatter=False, color='red')
    
    plt.title(f'Relationship: {x_col} vs {y_col}')
    
    return fig

def plot_box_plot_plt(df: pd.DataFrame, y_col: str, x_col: str = None):
    """Shows variance and outliers."""
    fig = plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=x_col, y=y_col, palette="Set2")
    
    plt.title(f'Box Plot of {y_col}' + (f' across {x_col}' if x_col else ""))
    
    return fig
    
