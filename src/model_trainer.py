from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_and_evaluate_model(df):
    """
    Trains a Logistic Regression model on the given DataFrame and evaluates its
    performance.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
    Returns: 
        None
    """
    print("\nTraining a simple Logistic Regression model...")
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression(solver='liblinear', random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy of the Logistic Regression model: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

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
    train_and_evaluate_model(df)