import pandas as pd



# Load dataset

df = pd.read_csv("ai_learning_lab.csv")



# 1. Print shape of dataset

print("Dataset Shape:")

print(df.shape)



# 2. Print first 5 rows

print("\nFirst 5 Rows:")

print(df.head())



# 3. Print column names

print("\nColumn Names:")

print(df.columns.tolist())



# 4. Print data types and dataset info

print("\nDataset Info:")

df.info()



# 5. Print missing value count

print("\nMissing Values Count:")

print(df.isnull().sum())



# 6. Print number of duplicate rows

print("\nDuplicate Rows Count:")

print(df.duplicated().sum())



# 7. Print value counts of topic column

print("\nTopic Value Counts:")

print(df["topic"].value_counts())



# 8. Print value counts of attendance column

print("\nAttendance Value Counts:")

print(df["attendance"].value_counts())
