import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Define features and target
    X = df.drop('Job_Satisfaction', axis=1)
    y = df['Job_Satisfaction']
    
    # Identify numerical and categorical columns
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = X.select_dtypes(include=['object']).columns
    
    # Create preprocessing pipelines
    num_pipeline = Pipeline([
        ('scaler', StandardScaler())
    ])
    
    cat_pipeline = Pipeline([
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    preprocessor = ColumnTransformer([
        ('num', num_pipeline, num_cols),
        ('cat', cat_pipeline, cat_cols)
    ])
    
    return X, y, preprocessor

def save_preprocessor(preprocessor, path):
    joblib.dump(preprocessor, path)

if __name__ == "__main__":
    # Example usage
    df = load_data('../data/raw/job_satisfaction.csv')
    X, y, preprocessor = preprocess_data(df)
    
    # Save preprocessing pipeline
    save_preprocessor(preprocessor, '../models/preprocessor.pkl')
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Save processed data
    X_train.to_csv('../data/processed/X_train.csv', index=False)
    X_test.to_csv('../data/processed/X_test.csv', index=False)
    y_train.to_csv('../data/processed/y_train.csv', index=False)
    y_test.to_csv('../data/processed/y_test.csv', index=False)