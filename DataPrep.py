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

import numpy as np
import pandas as pd
import statsmodels.api as sm

# Assume DataCleaned is a pandas DataFrame with columns: "Salary", "Age"

boot_samples = 1000
boot_results = np.zeros((boot_samples, 2))   # intercept + slope
boot_data = []       # to store bootstrap samples
boot_models = []     # to store fitted models

n = len(DataCleaned)

for i in range(boot_samples):

    # Bootstrap sample (same size as original)
    samp_idx = np.random.choice(n, n, replace=True)
    boot_df = DataCleaned.iloc[samp_idx].copy()
    boot_data.append(boot_df)

    # Fit regression Salary ~ Age
    X = sm.add_constant(boot_df["Age"])   # add intercept
    y = boot_df["Salary"]
    
    model = sm.OLS(y, X).fit()
    boot_models.append(model)

    # Store coefficients
    boot_results[i, :] = model.params.values

# ===================================
# View first bootstrap regression model
# ===================================
first_model = boot_models[0]
print(first_model.summary())

# (Optional) View first bootstrap dataset
# print(boot_data[0].head())


# ============================================================
# Model evaluation (RMSE computation)
# ============================================================

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Example: assume DataCleaned is a pandas DataFrame with columns 'Salary', 'Age', 'Experience'
# DataCleaned = pd.read_csv("your_data.csv")  

boot_samples = 1000  # number of bootstrap samples
n = len(DataCleaned)

# Store results
coef_list = []
rmse_list = []
r2_list = []

for i in range(boot_samples):
    # Bootstrap sample
    boot_data = DataCleaned.sample(n=n, replace=True)
    
    # Regression: Salary ~ Age + Experience
    X = boot_data[['Age', 'Experience']]
    X = sm.add_constant(X)  # adds intercept
    y = boot_data['Salary']
    
    model = sm.OLS(y, X).fit()
    
    # Store coefficients
    coef_list.append(model.params.values)
    
    # Compute predictions and RMSE
    y_pred = model.predict(X)
    rmse = np.sqrt(np.mean((y - y_pred)**2))
    rmse_list.append(rmse)
    
    # Store R-squared
    r2_list.append(model.rsquared)

# Convert results to DataFrame for easy analysis
boot_results = pd.DataFrame(coef_list, columns=['Intercept', 'Age', 'Experience'])
boot_results['RMSE'] = rmse_list
boot_results['R2'] = r2_list

# Example visualizations
plt.hist(boot_results['RMSE'], bins=30, color='skyblue', edgecolor='black')
plt.title('Bootstrap RMSE Distribution')
plt.xlabel('RMSE')
plt.ylabel('Frequency')
plt.show()

plt.hist(boot_results['R2'], bins=30, color='lightgreen', edgecolor='black')
plt.title('Bootstrap R² Distribution')
plt.xlabel('R²')
plt.ylabel('Frequency')
plt.show()

# ============================================================
# End of Script
# ============================================================


