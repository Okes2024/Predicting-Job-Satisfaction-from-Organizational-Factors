import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_model():
    # Load processed data
    X_train = pd.read_csv('../data/processed/X_train.csv')
    y_train = pd.read_csv('../data/processed/y_train.csv').squeeze()
    
    # Load preprocessor
    preprocessor = joblib.load('../models/preprocessor.pkl')
    
    # Transform training data
    X_train_transformed = preprocessor.fit_transform(X_train)
    
    # Initialize and train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_transformed, y_train)
    
    # Save model
    joblib.dump(model, '../models/job_satisfaction_model.pkl')
    
    # Evaluate training performance
    train_preds = model.predict(X_train_transformed)
    print(f"Training R²: {r2_score(y_train, train_preds):.4f}")
    print(f"Training RMSE: {mean_squared_error(y_train, train_preds, squared=False):.4f}")

if __name__ == "__main__":
    train_model()