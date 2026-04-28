import pandas as pd
import matplotlib.pyplot as plt
import os

def graph_csv(filename, x_column, y_column, title="Data Graph", xlabel="X-axis", ylabel="Y-axis"):
    """
    Reads a CSV file and plots a line graph.

    Args:
        filename (str): The name of the CSV file.
        x_column (str): The name of the column for the x-axis.
        y_column (str): The name of the column for the y-axis.
        title (str): The title of the graph.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return

    try:
        # Load data from the CSV file using pandas
        df = pd.read_csv(filename)

        # Check if columns exist
        if x_column not in df.columns or y_column not in df.columns:
            print(f"Error: Columns '{x_column}' or '{y_column}' not found in the CSV file.")
            print(f"Available columns: {list(df.columns)}")
            return

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(df[x_column], df[y_column], marker='o') # You can change 'marker' or chart type (e.g., plt.bar for bar chart)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.xticks(rotation=45) # Rotate x-axis labels for better readability if they are long (like dates)
        plt.tight_layout() # Adjust layout to prevent clipping of labels
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---
# Make sure you have a CSV file named 'data.csv' in the same directory
# with columns like 'Date' and 'Price'.

# Example: Plotting 'Price' over 'Date'
# Replace 'data.csv', 'Date', and 'Price' with your actual file name and column names.
graph_csv(
    filename='data.csv',
    x_column='Date',
    y_column='Price',
    title='Price Trend Over Time',
    xlabel='Date',
    ylabel='Price ($)'
)
