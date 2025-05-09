# Heart Disease Prediction Project

This Python-based data science project analyses a heart disease dataset and trains a Logistic Regression model to predict the presence of heart disease, using data preprocessing, Exploratory Data Analysis (EDA), and machine learning. The code is structured for use in vscode and consists of modular .py script files.

---

## Objective

Explore and model the "Heart Disease UCI" dataset to identify key features affecting patients' health conditions and build a machine learning model for prediction. 

---

## Dataset

The dataset used is the "Heart Disease UCI" dataset, which can be found on Kaggle (you will need to download `heart.csv` and place it in the same directory as the Python script). It contains various features related to patients' health conditions and a binary target variable indicating the presence or absence of heart disease. It is used to to explore data cleaning, visualization, and machine learning for survival prediction.

---

## Project Structure

heart_disease_project/
├── src
    └── data/     : Stores heart disease dataset in CSV file format
        └── heart.cvs : Heart disease dataset
    └── figures/  : Stores images     
    └── models/   : Strores models   
    └── data_loader.py: For data loading and preprocessing.
    └── eda.py: For Exploratory Data Analysis.
    └── main.py: The main script to orchestrate the execution.
    └── model_trainer.py: For model training.
├── .gitignore    : Project documentation
├── Heart_Disease_Prediction_Presentation.pptx
├── LICENCE
├── README.md
└── requirements.txt : List of Python dependencies  

---

## Technologies Used: 

- Python 3.8+
- pandas, numpy
- seaborn, matplotlib
- scikit-learn, joblib
- powerpoint
- csv file
- vscode

---

## Setup Instructions

1. **Clone the repository**

```
https://github.com/AAdewunmi/Heart-Disease-Prediction-Analysis-Project.git
```

2. **Create a virtual environment (macOS/Linux)**

```bash
# Set up virtual environment
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run scripts
python data_loader.py
python eda.py
python model_trainer.py
python main.py
```
---

## Output

The script will:

* Print basic information about the dataset.
* Generate and save several Exploratory Data Analysis (EDA) visualizations as `.png` files (e.g., distribution of the target variable, histograms of numerical features, a scatter plot, and a correlation matrix).
* Train a Logistic Regression model on the data.
* Print the accuracy, classification report, and confusion matrix of the model on the test set.

---

## Visualizations

---

## Next Steps (Potential Improvements)

* Explore other classification models (e.g., Random Forest, Support Vector Machines).
* Perform feature scaling and selection.
* Conduct more in-depth EDA.
* Fine-tune the model hyperparameters.

---

## Power Point Presentation Outline

Here is an outline of a power point presentation for this project. 

[Heart Disease Prediction Project](Heart_Disease_Prediction_Presentation.pptx)

---

## Contact
If you have questions or suggestions, feel free to reach out or open an issue.

---

## Author

Adrian Adewunmi – [GitHub](https://github.com/AAdewunmi)