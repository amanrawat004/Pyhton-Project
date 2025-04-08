import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\abhay\Downloads\kaam\RTA Dataset.csv")



# Show first few rows
print(df.head())

# Objective 1: Gender distribution
print(df['Sex_of_casualty'].value_counts())

# Objective 2: Accident involvement by age group
print(df['Age_band_of_casualty'].value_counts())

# Objective 3: Most affected occupation group
print(df['Educational_level'].value_counts())

# Objective 4: Education level vs accident occurrence
print(df.groupby('Educational_level')['Accident_severity'].value_counts())
