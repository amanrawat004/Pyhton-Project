import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\abhay\Downloads\kaam\RTA Dataset.csv")

# Initial inspection
print("Initial shape:", df.shape)
print("\nMissing values per column:")
print(df.isnull().sum())

# Replace inconsistent missing values with np.nan
df.replace(['', ' ', 'na'], np.nan, inplace=True)

# Strip whitespace and standardize text
string_cols = df.select_dtypes(include='object').columns
df[string_cols] = df[string_cols].apply(lambda x: x.str.strip().str.title() if x.dtype == "object" else x)

# Convert 'Time' to datetime safely
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').dt.time

# Fix specific values
df['Service_year_of_vehicle'] = df['Service_year_of_vehicle'].str.replace('yrs', 'yr', regex=False)
df['Service_year_of_vehicle'] = df['Service_year_of_vehicle'].str.replace('s', '', regex=False)

df['Age_band_of_driver'] = df['Age_band_of_driver'].str.replace('Under', 'Under 18')
df['Age_band_of_driver'] = df['Age_band_of_driver'].str.replace('Over', 'Over 51')
df['Casualty_severity'] = df['Casualty_severity'].replace({'1': 'Slight Injury', '2': 'Serious Injury', '3': 'Fatal Injury'})

# Standardize known inconsistencies
vehicle_mapping = {
    'Lorry (41?100Q)': 'Lorry (41-100Q)',
    'Lorry (11?40Q)': 'Lorry (11-40Q)',
    'Public (> 45 Seats)': 'Public (> 45 seats)',
    'Public (13?45 Seats)': 'Public (13-45 seats)',
    'Public (12 Seats)': 'Public (12 seats)',
    'Pick Up Upto 10Q': 'Pick up upto 10Q',
    'Stationwagon': 'Stationwagen'
}
df['Type_of_vehicle'] = df['Type_of_vehicle'].replace(vehicle_mapping)

road_cond_mapping = {
    'Wet Or Damp': 'Wet or damp',
    'Flood Over 3cm. Deep': 'Flooded'
}
df['Road_surface_conditions'] = df['Road_surface_conditions'].replace(road_cond_mapping)

# Fill missing values for relevant categorical columns
categorical_fill_cols = [
    'Sex_of_driver', 'Educational_level', 'Vehicle_driver_relation',
    'Type_of_vehicle', 'Owner_of_vehicle', 'Defect_of_vehicle',
    'Area_accident_occured', 'Types_of_Junction', 'Road_surface_type',
    'Road_surface_conditions', 'Light_conditions', 'Weather_conditions',
    'Type_of_collision', 'Cause_of_accident', 'Driving_experience',
    'Lanes_or_Medians', 'Road_allignment', 'Casualty_class',
    'Sex_of_casualty', 'Age_band_of_casualty', 'Casualty_severity',
    'Work_of_casualty', 'Fitness_of_casualty', 'Vehicle_movement'
]

for col in categorical_fill_cols:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown')

# Fill specific column with 'Unknown' (if still NaN)
df['Service_year_of_vehicle'] = df['Service_year_of_vehicle'].fillna('Unknown')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Final inspection
print("\nAfter cleaning - shape:", df.shape)
print("\nMissing values per column after cleaning:")
print(df.isnull().sum())

# Save cleaned data
df.to_csv(r'C:\Users\abhay\Downloads\kaam\RTA Dataset.csv', index=False)
print("\nData cleaning complete. Cleaned data saved to 'RTA Dataset.csv'")

#Problem Statement 1: Accident Severity and Demographics

# 1. Frequency of each severity type
print(df['Accident_severity'].value_counts())

# 2. Average age of victims per severity
age_map = {
    'Under 18': 15, '18-30': 24, '31-50': 40,
    'Over 51': 60, 'Unknown': None
}
df['Age_band_numeric'] = df['Age_band_of_casualty'].map(age_map)
print(df.groupby('Accident_severity')['Age_band_numeric'].mean())

# 3. Severity vs vehicle type
print(df.groupby('Type_of_vehicle')['Accident_severity'].value_counts())

# 4. Severity across road user categories
print(df.groupby('Casualty_class')['Accident_severity'].value_counts())

 #Problem Statement 2: Driver Demographics and Accident Types
# 1. Driver sex vs accident severity
print(df.groupby('Sex_of_driver')['Accident_severity'].value_counts())

# 2. Education level vs accident severity
print(df.groupby('Educational_level')['Accident_severity'].value_counts())

# 3. Driving experience vs accident severity
print(df.groupby('Driving_experience')['Accident_severity'].value_counts())

# 4. Driver age group vs type of collision
print(df.groupby('Age_band_of_driver')['Type_of_collision'].value_counts())

#Problem Statement 3: Road and Environmental Conditions
# 1. Road surface type vs severity
print(df.groupby('Road_surface_type')['Accident_severity'].value_counts())

# 2. Weather conditions vs severity
print(df.groupby('Weather_conditions')['Accident_severity'].value_counts())

# 3. Light conditions vs severity
print(df.groupby('Light_conditions')['Accident_severity'].value_counts())

# 4. Road alignment vs severity
print(df.groupby('Road_allignment')['Accident_severity'].value_counts())

# Problem Statement 4: Vehicle and Movement Patterns

# 1. Vehicle movement vs severity
print(df.groupby('Vehicle_movement')['Accident_severity'].value_counts())

# 2. Type of vehicle vs cause of accident
print(df.groupby('Type_of_vehicle')['Cause_of_accident'].value_counts())

# 3. Owner of vehicle vs severity
print(df.groupby('Owner_of_vehicle')['Accident_severity'].value_counts())

# 4. Vehicle driver relation vs severity
print(df.groupby('Vehicle_driver_relation')['Accident_severity'].value_counts())

# ----------------- Visualization Section ------------------

# Encode values for plots
df['Severity_encoded'] = df['Accident_severity'].map({'Slight Injury': 1, 'Serious Injury': 2, 'Fatal Injury': 3})
df['Age_numeric'] = df['Age_band_of_driver'].map({'Under 18': 15, '18-30': 24, '31-50': 40, 'Over 51': 60, 'Unknown': None})

# SCATTER PLOT: Age vs Severity
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age_numeric', y='Severity_encoded', hue='Sex_of_driver', data=df)
plt.title("Scatter Plot: Age vs Accident Severity")
plt.xlabel("Age (Approx.)")
plt.ylabel("Severity (Encoded)")
plt.show()

# BAR PLOT: Education vs Avg Severity
plt.figure(figsize=(10, 6))
sns.barplot(x='Educational_level', y='Severity_encoded', data=df, estimator=lambda x: sum(x)/len(x))
plt.title("Bar Plot: Education Level vs Average Severity")
plt.xticks(rotation=45)
plt.show()

# BOX PLOT: Age vs Severity
plt.figure(figsize=(8, 6))
sns.boxplot(x='Accident_severity', y='Age_numeric', data=df)
plt.title("Box Plot: Age Distribution per Severity Level")
plt.show()

# LINE CHART: Accidents over weekdays
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['Day_of_week'] = pd.Categorical(df['Day_of_week'], categories=weekday_order, ordered=True)
weekday_counts = df['Day_of_week'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.plot(weekday_counts.index, weekday_counts.values, marker='o', linestyle='-')
plt.title("Line Chart: Accidents Over Days of the Week")
plt.xlabel("Day of Week")
plt.ylabel("Number of Accidents")
plt.grid()
plt.show()

# STRIP PLOT: Top 5 vehicle types vs Severity
top_vehicles = df['Type_of_vehicle'].value_counts().head(5).index
filtered_df = df[df['Type_of_vehicle'].isin(top_vehicles)]

plt.figure(figsize=(8, 6))
sns.stripplot(x='Type_of_vehicle', y='Severity_encoded', data=filtered_df, jitter=True)
plt.title("Strip Plot: Severity Distribution in Top 5 Vehicle Types")
plt.xticks(rotation=45)
plt.show()

# PAIR PLOT
pair_df = df[['Age_numeric', 'Severity_encoded']].dropna()
sns.pairplot(pair_df)
plt.suptitle("Pair Plot: Age and Severity", y=1.02)
plt.show()

# DONUT CHART: Road surface conditions
road_counts = df['Road_surface_conditions'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(road_counts, labels=road_counts.index, startangle=90, wedgeprops=dict(width=0.4))
plt.title("Donut Chart: Road Surface Conditions")
plt.show()

# PIE CHART: Light conditions
light_counts = df['Light_conditions'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(light_counts, labels=light_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart: Light Conditions Distribution")
plt.show()

# HEATMAP
corr_df = df[['Age_numeric', 'Severity_encoded']].corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corr_df, annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Heatmap: Correlation Matrix")
plt.show()
