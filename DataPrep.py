# ============================================================
# Loading packages
# ============================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils import resample
import statsmodels.api as sm
from scipy.stats import shapiro

# ============================================================
# Reading the dataset
# ============================================================

# Load Excel data (same as read_excel in R)
Data_to_clean = pd.read_excel("Data_Cleaning.xlsx")
print(Data_to_clean)

# ============================================================
# Summarizing variables with count
# ============================================================

print(Data_to_clean['Gender'].value_counts())
print(Data_to_clean['Age'].value_counts())
print(Data_to_clean['Status'].value_counts())

# ============================================================
# Workflow: Data Cleaning
# ============================================================

# Reload data
Data_to_clean = pd.read_excel("Data_Cleaning.xlsx")

# Remove rows with missing Status
DataCleaned = Data_to_clean[~Data_to_clean['Status'].isna()]

# Remove duplicate rows
DataCleaned = DataCleaned.drop_duplicates()

# Correcting spelling errors in Gender
DataCleaned['Gender'] = DataCleaned['Gender'].replace({
    'Female': 'female',
    'femail': 'female'
})

# Replace placeholder (999) with NaN
DataCleaned['Age'] = DataCleaned['Age'].replace(999, np.nan)

# ============================================================
# Impute missing values
# ============================================================

# Impute with mean
DataCleaned['Age'] = DataCleaned['Age'].fillna(round(DataCleaned['Age'].mean()))

# Or impute with median (alternative)
# DataCleaned['Age'] = DataCleaned['Age'].fillna(DataCleaned['Age'].median())

print(DataCleaned)

# ============================================================
# Boxplot: Gender vs Age
# ============================================================

sns.boxplot(x='Gender', y='Age', data=DataCleaned)
plt.title("Comparative Boxplot Gender vs Age")
plt.show()

# ============================================================
# Adding a height variable
# ============================================================

DataCleaned['Height_cm'] = [160, 175, 155, 165, 178, 190, 191, 180, 159, 167, 167]
print(DataCleaned)

# ============================================================
# Scatter plot: Age vs Height
# ============================================================

sns.scatterplot(x='Age', y='Height_cm', data=DataCleaned)
plt.title("Scatter plot Age vs Height")
plt.show()

# ============================================================
# Log transformation
# ============================================================

DataCleaned['Log_Age'] = np.log(DataCleaned['Age'])
print(DataCleaned)

# Scatter plot: Log Age vs Height
sns.scatterplot(x='Log_Age', y='Height_cm', data=DataCleaned)
plt.title("Scatter plot Log Age vs Height")
plt.show()

# ============================================================
# Simple Linear Regression: Height ~ Log_Age
# ============================================================

X = sm.add_constant(DataCleaned['Log_Age'])
y = DataCleaned['Height_cm']
lm_r = sm.OLS(y, X).fit()
print(lm_r.summary())

# ============================================================
# Adding a Salary variable
# ============================================================

DataCleaned['Salary'] = [35, 22, 55, 25, 23, 20, 40, 45, 25, 19, 41]
print(DataCleaned)

# ============================================================
# Creating a bootstrap sample
# ============================================================

import numpy as np

bootstrap_samples = [
    DataCleaned.sample(
        n=len(DataCleaned), 
        replace=True
    )
    for _ in range(1000)
]

# ============================================================
# Bootstrapping process: Multiple Linear Regression
# ============================================================

boot_samples = 1000
boot_results = np.zeros((boot_samples, 2))

for i in range(boot_samples):
    samp = resample(DataCleaned, replace=True)
    X = sm.add_constant(samp['Age'])
    y = samp['Salary']
    model = sm.OLS(y, X).fit()
    boot_results[i, :] = model.params.values

# View the first few coefficient estimates
print(boot_results[:5, :])

# ============================================================
# Model evaluation (RMSE computation)
# ============================================================

OrigDataSel = DataCleaned[['Age']].values
Pred = np.zeros((boot_results.shape[0], OrigDataSel.shape[0]))

for i in range(boot_results.shape[0]):
    intercept, slope = boot_results[i, :]
    Pred[i, :] = intercept + slope * OrigDataSel.flatten()

Act = np.tile(DataCleaned['Salary'].values, (boot_results.shape[0], 1))
residuals = Act - Pred
ErrSq = residuals**2
SSE = ErrSq.sum(axis=1)
MSE = SSE / len(DataCleaned)
RMSE = np.sqrt(MSE)

plt.hist(RMSE, bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of RMSE (Bootstrap)")
plt.show()

# Shapiro-Wilk normality test for RMSE
stat, p = shapiro(RMSE)
print(f"Shapiro-Wilk Test: Statistic={stat:.3f}, p-value={p:.3f}")

