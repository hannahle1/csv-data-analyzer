import pandas as pd
def analyze_csv(file_path):
    print("=" * 50)
    print(f"ANALYZING DATASET: {file_path}")
    print("=" * 50)

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        # prevent the program from crashing abrubtly if the file doesn't exist or if the file name is wrong
        # instead of crashing, it catches the error, prints a friendly warning message, and returns
        print(f"Error: The file '{file_path}' was not found.")
        return

    # Basic overview 
    print("\nFIRST 5 ROWS: ")
    print(df.head())
    print("\nDATASET DIMENSIONS: ")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    # Statistical summary
    print("\nSTATISTICAL SUMMARY: ")
    print(df.describe())

    # 3. Custom Insights 
    print("Columns available:", list(df.columns))

    print("=" * 50)
    print("ANALYSIS COMPLETE!")
    print("=" * 50)

if __name__ == "__main__":
    analyze_csv("Top_Movies_dataset.csv")
