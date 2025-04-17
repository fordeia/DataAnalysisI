import pandas as pd
import numpy as np

# Read the excel file
df = pd.read_excel(r"C:\Users\fordeia\DataAnalysisI\Data_Cleaning.xlsx")

df_cleaned = df

# Rename levels in 'col1'
df_cleaned['Gender'] = df_cleaned['Gender'].replace({'Female': 'female', 'femail': 'female'})

# Remove duplicate rows based on all columns
df_cleaned = df_cleaned.drop_duplicates()

df_cleaned = df_cleaned.replace(999, np.nan)

df_cleaned.dropna(subset=['Status'], inplace=True)

# Mean imputation
df_mean_imputed = df_cleaned.copy()
df_mean_imputed['Age'].fillna(df_mean_imputed['Age'].mean(), inplace=True)
print("\nDataFrame after mean imputation:\n", round(df_mean_imputed))

# Median imputation
df_median_imputed = df_cleaned.copy()
df_median_imputed['Age'].fillna(df_median_imputed['Age'].median(), inplace=True)
print("\nDataFrame after median imputation:\n", df_median_imputed)
