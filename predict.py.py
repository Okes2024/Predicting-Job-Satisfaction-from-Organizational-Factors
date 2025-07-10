# Exploratory Data Analysis and Preprocessing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('../data/raw/job_satisfaction.csv')

# 1. Basic inspection
print(df.info())
print(df.describe())

# 2. Target distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Job_Satisfaction'], kde=True)
plt.title('Job Satisfaction Distribution')
plt.show()

# 3. Correlation analysis
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Feature Correlations')
plt.show()

# 4. Categorical relationships
fig, ax = plt.subplots(2, 2, figsize=(15, 10))
sns.boxplot(x='Workplace_Culture', y='Job_Satisfaction', data=df, ax=ax[0,0])
sns.boxplot(x='Management_Quality', y='Job_Satisfaction', data=df, ax=ax[0,1])
sns.boxplot(x='Career_Growth', y='Job_Satisfaction', data=df, ax=ax[1,0])
plt.tight_layout()
plt.show()