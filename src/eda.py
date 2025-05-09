import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


def perform_eda(df):
    """
    Performs basic Exploratory Data Analysis (EDA) on the provided DataFrame
    by:
    - Visualizing the target variable distribution
    - Plotting histograms for key numerical features
    - Displaying a scatter plot between cholesterol and resting blood pressure
    - Generating a correlation heatmap

    The plots are saved as PNG files in the 'figures/' directory.

    Args:
        df (pandas.DataFrame): The DataFrame containing the heart disease
            dataset.

    Example:
        df = load_and_preprocess_data('data/heart.csv')
        if df is not None:
            perform_eda(df)
    """

    print("\nPerforming Exploratory Data Analysis...")

    # Ensure the output directory exists
    os.makedirs('figures', exist_ok=True)

    # Plot distribution of the target variable (AHD: presence of heart disease)
    plt.figure(figsize=(6, 4))
    sns.countplot(x='AHD', data=df)
    plt.title('Distribution of Heart Disease (0 = No Disease, 1 = Disease)')
    plt.xlabel('Heart Disease')
    plt.ylabel('Count')
    plt.savefig('figures/eda_target_distribution.png')
    plt.close()

    # Define selected numerical columns for histogram plots
    numerical_features = ['Age', 'RestBP', 'Chol', 'MaxHR', 'Oldpeak']


    # Plot histogram for each numerical feature
    for col in numerical_features:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.savefig(f'figures/eda_histogram_{col}.png')
        plt.close()

    # Scatter plot showing the relationship between cholesterol and resting BP,
    # colored by disease presence
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='RestBP', y='Chol', hue='AHD', data=df)
    plt.title('Cholesterol vs. Resting Blood Pressure')
    plt.xlabel('Resting Blood Pressure (trestbps)')
    plt.ylabel('Cholesterol (chol)')
    plt.legend(title='Heart Disease', labels=['No', 'Yes'])
    plt.savefig('figures/eda_scatter_chol_trestbps.png')
    plt.close()

    # Compute correlation matrix for numerical features only
    numeric_df = df.select_dtypes(include=['number'])
    correlation_matrix = numeric_df.corr()

    # Plot heatmap of the correlation matrix
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Features')
    plt.savefig('figures/eda_correlation_matrix.png')
    plt.close()
