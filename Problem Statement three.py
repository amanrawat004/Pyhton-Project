import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\abhay\Downloads\kaam\RTA Dataset.csv")

# Show first few rows
print(df.head())

# Objective 1: Accidents by light condition
print(df['Light_conditions'].value_counts())

# Objective 2: Accidents by weather
print(df['Weather_conditions'].value_counts())

# Objective 3: Environmental condition vs severity
print(df.groupby('Weather_conditions')['Accident_severity'].value_counts())

# Objective 4: Accidents by time of day
print(df['Time'].value_counts().sort_index())
