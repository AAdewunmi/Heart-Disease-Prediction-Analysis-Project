import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    """
    Performs Exploratory Data Analysis (EDA) on the given DataFrame and saves
    visualizations as PNG files.

    Args:
        df (pandas.DataFrame): The DataFrame to analyze.
    """
    print("\nPerforming Exploratory Data Analysis...")

    # Distribution of the target variable
    plt.figure(figsize=(6, 4))
    sns.countplot(x='target', data=df)
    plt.title('Distribution of Heart Disease (0 = No Disease, 1 = Disease)')
    plt.xlabel('Heart Disease')
    plt.ylabel('Count')
    plt.savefig('/figures/eda_target_distribution.png')
    print("Saved: eda_target_distribution.png")
    plt.close()

    # Histograms of numerical features
    numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    for col in numerical_features:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.savefig(f'/figures/eda_histogram_{col}.png')
        print(f"Saved: eda_histogram_{col}.png")
        plt.close()

    # Scatter plot of cholesterol vs. blood pressure
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='trestbps', y='chol', hue='target', data=df)
    plt.title('Cholesterol vs. Resting Blood Pressure')
    plt.xlabel('Resting Blood Pressure (trestbps)')
    plt.ylabel('Cholesterol (chol)')
    plt.legend(title='Heart Disease', labels=['No', 'Yes'])
    plt.savefig('/figures/eda_scatter_chol_trestbps.png')
    print("Saved: eda_scatter_chol_trestbps.png")
    plt.close()

    # Correlation matrix
    correlation_matrix = df.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Features')
    plt.savefig('/figures/eda_correlation_matrix.png')
    print("Saved: eda_correlation_matrix.png")
    plt.close()

if __name__ == '__main__':
    # added to run the file independently
    import pandas as pd
    # Create a sample DataFrame (replace with your actual data loading)
    data = {'age': [63, 67, 41, 56, 57, 57, 56, 66, 60, 57, 64, 56, 64, 56, 67],
            'trestbps': [145, 160, 130, 120, 130, 150, 130, 150, 150, 140, 110, 140, 160, 120, 120],
            'chol': [233, 286, 204, 236, 250, 168, 294, 262, 232, 210, 214, 294, 267, 199, 229],
            'thalach': [150, 108, 172, 178, 174, 174, 153, 114, 171, 130, 168, 150, 148, 162, 129],
            'oldpeak': [2.3, 1.5, 1.4, 0.8, 1.6, 0.4, 1.3, 2.6, 0.0, 1.0, 1.2, 0.0, 3.6, 0.0, 2.6],
            'target': [1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]}
    df = pd.DataFrame(data)
    perform_eda(df)