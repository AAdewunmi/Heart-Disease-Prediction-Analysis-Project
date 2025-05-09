from data_loader import load_and_preprocess_data
from eda import perform_eda
from model_trainer import train_and_evaluate_model


def main():
    """
    Coordinates the entire machine learning workflow:
    1. Loads and preprocesses the heart disease dataset.
    2. Performs Exploratory Data Analysis (EDA) and saves plots.
    3. Trains a Logistic Regression model and saves the trained model 
       and features.

    This function is designed to be the entry point of the application.

    Example:
        To run the full pipeline, simply execute the script:
        $ python main.py
    """
    # Step 1: Load and clean the dataset
    df = load_and_preprocess_data()

    # Proceed only if data is successfully loaded
    if df is not None:
        # Step 2: Run Exploratory Data Analysis (EDA)
        perform_eda(df)

        # Step 3: Train and evaluate the model, then save it
        train_and_evaluate_model(df)

# This ensures the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
