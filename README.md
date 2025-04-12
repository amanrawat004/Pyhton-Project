
# Road Traffic Accidents (RTA) - Exploratory Data Analysis

## 📊 Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on a dataset of Road Traffic Accidents (RTA) in order to identify key patterns, correlations, and insights into the causes and severity of road accidents. Through data cleaning, feature standardization, and the application of various visualization techniques using `Seaborn` and `Matplotlib`, the goal is to understand accident characteristics and their contributing factors.

## 📁 Source of Dataset

The dataset was sourced from Kaggle: [Road Traffic Accidents Dataset](https://www.kaggle.com/datasets/saurabhshahane/road-traffic-accidents)

## 🧹 EDA Process Followed

1. **Data Cleaning:**
   - Standardized column formats and fixed inconsistent entries.
   - Replaced empty strings, whitespace, and 'na' values with NaN.
   - Converted date/time and categorical features to proper formats.
   - Fixed issues with inconsistent values across columns.
   - Encoded necessary fields for plotting and analysis.

2. **Handling Missing Values:**
   - Filled missing categorical values with 'Unknown' where suitable.
   - Cleaned and imputed columns like `Driving_experience`, `Casualty_class`, `Fitness_of_casuality`, etc.

3. **Visualization:**
   - Used Seaborn and Matplotlib for visualizing relationships between features and accident severity.
   - Charts include bar plots, scatter plots, box plots, line charts, strip plots, swarm plots, pair plots, pie charts, donut charts, and heatmaps.

## 📌 Problem Statements and Objectives

1. **Accident Severity Distribution:**  
   - Analyze accident counts by severity.
   - Identify top contributing factors.
   - Visualize severity by day of week and area.
   - Explore severity with relation to light and weather conditions.

2. **Driver Attributes and Accident Severity:**  
   - Analyze severity based on sex and age of drivers.
   - Study correlation with educational level and driving experience.
   - Visualize trends across different categories.

3. **Vehicle and Road Condition Factors:**  
   - Understand impact of vehicle type and defect.
   - Analyze service years and ownership in accidents.
   - Study road type, surface, and junction types.

4. **Casualty and Collision Analysis:**  
   - Assess casualty classes and their severity.
   - Study movement and condition of casualties.
   - Understand pedestrian involvement.

5. **Advanced Visualization with Seaborn:**  
   - Scatter plot: Age vs Severity.
   - Bar plot: Road alignment vs Severity.
   - Box plot: Driver age by vehicle type.
   - Strip plot: Weather vs Severity.

6. **Advanced Visualization with Matplotlib:**  
   - Swarm plot: Weather vs Severity.
   - Pair plot: Age and Severity encoding.
   - Donut chart: Road surface conditions.
   - Pie chart: Light conditions.
   - Heatmap: Correlation matrix.

## 📌 Key Libraries Used

- `pandas` and `numpy` for data handling
- `matplotlib.pyplot` and `seaborn` for visualization

## ✅ Conclusion

This analysis revealed that driver inexperience, environmental conditions, and poor road surfaces are major contributors to traffic accident severity. The use of visualizations helped in identifying hidden patterns that may guide policy-making and safety improvements.
