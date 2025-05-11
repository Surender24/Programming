import pandas as pd

# Load the dataset
df = pd.read_csv('student.csv')

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing Age or Marks
df_cleaned = df.dropna(subset=['Age', 'Marks'])

# Remove duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

# Convert Age to integer
df_cleaned['Age'] = df_cleaned['Age'].astype(int)

print(df_cleaned)
