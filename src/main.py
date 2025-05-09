from data_loader import load_and_preprocess_data
from eda import perform_eda
from model_trainer import train_and_evaluate_model

def main():
    """
    Main function to orchestrate the data loading, EDA, and model training.
    """
    df = load_and_preprocess_data()
    if df is not None: # only proceeds if data loading was successful
        perform_eda(df)
        train_and_evaluate_model(df)

if __name__ == "__main__":