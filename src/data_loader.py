import pandas as pd


def load_and_preprocess_data(csv_file='/data/heart.csv'):
    """
    Loads the heart disease dataset from a CSV file and performs basic preprocessing.

    Args:
        csv_file (str, optional): The path to the CSV file. Defaults to 'heart.csv'.

    Returns:
        pandas.DataFrame: The preprocessed DataFrame.  Returns None and prints an
                          error message if the file is not found.
    """
    print("Loading and preprocessing data...")
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: '{csv_file}' not found.  Please ensure the file is in the same directory.")
        return None

    print("\nFirst 5 rows of the dataframe:")
    print(df.head())
    print("\nInformation about the dataframe:")
    print(df.info())
    print("\nSummary statistics:")
    print(df.describe())

    print("\nMissing values:")
    print(df.isnull().sum())
    return df

if __name__ == '__main__':
    # added to run the file independently
    df = load_and_preprocess_data()
    if df is not None:
        print("Data loaded and preprocessed successfully.")