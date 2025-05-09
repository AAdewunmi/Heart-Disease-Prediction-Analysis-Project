from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.impute import SimpleImputer
import pandas as pd
import joblib
import os


def train_and_evaluate_model(df):
    """
    Trains and evaluates a Logistic Regression model using a cleaned heart 
    disease dataset.
    It also encodes categorical variables, handles missing data, and saves both 
    the trained model and the list of feature columns used in the model.

    Args:
        df (pandas.DataFrame): The preprocessed DataFrame that includes 
        features and the target column 'AHD' 
        (presence of heart disease).

    Saves:
        - Trained Logistic Regression model to: 
          'src/models/logistic_regression_model.pkl'
        - Model feature columns to: 'src/models/model_columns.pkl'

    Example:
        df = load_and_preprocess_data()
        if df is not None:
            train_and_evaluate_model(df)
    """
    print("\nTraining a simple Logistic Regression model...")

    # Separate features (X) and the target variable (y)
    X = df.drop('AHD', axis=1)
    y = df['AHD']

    # Identify column types
    numerical_cols = X.select_dtypes(include=['number']).columns
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns

    # Handle missing values in numerical columns using mean imputation
    imputer = SimpleImputer(strategy='mean')
    X[numerical_cols] = imputer.fit_transform(X[numerical_cols])

    # Convert categorical variables into dummy/indicator variables 
    # (one-hot encoding)
    X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

    # Split the data into training and test sets (70% train, 30% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.3, random_state=42
    )

    # Initialize and train the logistic regression model
    model = LogisticRegression(solver='liblinear', random_state=42)
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Prepare directory to save model and feature list
    model_dir = 'models'
    os.makedirs(model_dir, exist_ok=True)

    # Define paths for saving model and feature columns
    model_path = os.path.join(model_dir, 'logistic_regression_model.pkl')
    columns_path = os.path.join(model_dir, 'model_columns.pkl')

    # Save the model and the feature column names
    joblib.dump(model, model_path)
    joblib.dump(X_encoded.columns.tolist(), columns_path)

    print(f"\n✅ Model saved to: {model_path}")
    print(f"🧾 Model feature columns saved to: {columns_path}")
