import pandas as pd


def load_and_preprocess_data(csv_file='data/heart.csv'):
    """
    Loads the heart disease dataset from a CSV file and displays basic 
    information
    to help understand the structure and contents of the dataset.

    Args:
        csv_file (str, optional): Path to the CSV file containing the dataset.
                                  Defaults to 'data/heart.csv'.

    Returns:
        pandas.DataFrame: The loaded and raw DataFrame. 
        Returns None if the file is not found.

    Example:
        df = load_and_preprocess_data('data/heart.csv')
        if df is not None:
            print(df.shape)
    """
    print("Loading and preprocessing data...")

    # Try to read the CSV file into a DataFrame
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(
            f"Error: '{csv_file}' not found. Please ensure the file exists "
            f"at the specified path."
        )
        return None

    # Display the first few rows to get a glimpse of the data
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Print concise summary: column names, data types, and non-null counts
    print("\nDataFrame information:")
    print(df.info())

    # Show summary statistics for numeric columns
    print("\nSummary statistics for numeric features:")
    print(df.describe())

    # Display count of missing values per column
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    # Return the DataFrame for further processing
    return df
