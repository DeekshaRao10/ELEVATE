

import pandas as pd



def load_data(file_path):
    """Load CSV file into Pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.\n")
        return df
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return None



def explore_data(df):
    """Display basic dataset exploration."""
    print("First 5 rows:\n", df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nStatistical Summary:\n", df.describe())



def clean_missing_values(df):
    """Fill numeric NaN with mean and drop remaining missing rows."""
    df = df.copy()

    
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        df[col].fillna(df[col].mean(), inplace=True)

    
    df.dropna(inplace=True)

    print("\nMissing values handled.")
    return df



def filter_sort_data(df):
    """Example filter and sort."""
    if "marks" in df.columns:
        filtered = df[df["marks"] > 70]
        sorted_df = filtered.sort_values(by="marks", ascending=False)
        print("\nFiltered & Sorted Data:\n", sorted_df.head())
        return sorted_df
    else:
        print("\nColumn 'marks' not found. Skipping filter.")
        return df


def group_and_aggregate(df):
    """Group by a column and calculate average marks."""
    if "department" in df.columns and "marks" in df.columns:
        grouped = df.groupby("department")["marks"].mean()
        print("\nAverage Marks by Department:\n", grouped)
    else:
        print("\nRequired columns not found for grouping.")



def add_calculated_column(df):
    """Add grade column based on marks."""
    if "marks" in df.columns:
        df["grade"] = df["marks"].apply(
            lambda x: "A" if x >= 80 else
                      "B" if x >= 60 else
                      "C"
        )
        print("\nAdded 'grade' column.")
    return df



def export_data(df, output_file="cleaned_data.csv"):
    """Export DataFrame to CSV."""
    df.to_csv(output_file, index=False)
    print(f"\nCleaned data exported to {output_file}")



def main():
    file_path = input("Enter CSV file path: ")

    df = load_data(file_path)
    if df is None:
        return

    explore_data(df)

    df = clean_missing_values(df)

    df = filter_sort_data(df)

    group_and_aggregate(df)

    df = add_calculated_column(df)

    export_data(df)


if __name__ == "__main__":
    main()
