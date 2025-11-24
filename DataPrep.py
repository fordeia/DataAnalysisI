################################################################################
# 1. LOAD PACKAGES
################################################################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils import resample
import statsmodels.api as sm
from scipy.stats import shapiro

################################################################################
# 2. READ THE DATASET
################################################################################

# 2.1 Load Excel data
Data_to_clean = pd.read_excel("Data_Cleaning.xlsx")
print(Data_to_clean)

################################################################################
# 3. SUMMARIZE VARIABLES WITH COUNT
################################################################################

# 3.1 Count Gender
print(Data_to_clean['Gender'].value_counts())
# 3.2 Count Age
print(Data_to_clean['Age'].value_counts())
# 3.3 Count Status
print(Data_to_clean['Status'].value_counts())

################################################################################
# 4. DATA CLEANING WORKFLOW
################################################################################

# 4.1 Reload data
Data_to_clean = pd.read_excel("Data_Cleaning.xlsx")

# 4.2 Remove rows with missing Status
DataCleaned = Data_to_clean[~Data_to_clean['Status'].isna()]

# 4.3 Remove duplicate rows
DataCleaned = DataCleaned.drop_duplicates()

# 4.4 Correct spelling errors in Gender
DataCleaned['Gender'] = DataCleaned['Gender'].replace({
    'Female': 'female',
    'femail': 'female'
})

# 4.5 Replace placeholder (999) with NaN
DataCleaned['Age'] = DataCleaned['Age'].replace(999, np.nan)

################################################################################
# 5. HANDLE MISSING VALUES
################################################################################

# 5.1 Impute with mean
DataCleaned['Age'] = DataCleaned['Age'].fillna(round(DataCleaned['Age'].mean()))

# 5.2 Or impute with median (alternative)
# DataCleaned['Age'] = DataCleaned['Age'].fillna(DataCleaned['Age'].median())

print(DataCleaned)

################################################################################
# 6. BOX PLOT: GENDER VS AGE
################################################################################

sns.boxplot(x='Gender', y='Age', data=DataCleaned)
plt.title("Comparative Boxplot Gender vs Age")
plt.show()

################################################################################
# 7. ADD HEIGHT VARIABLE
################################################################################

DataCleaned['Height_cm'] = [160, 175, 155, 165, 178, 190, 191, 180, 159, 167, 167, 159]
print(DataCleaned)

################################################################################
# 8. SCATTER PLOT: AGE VS HEIGHT
################################################################################

sns.scatterplot(x='Age', y='Height_cm', data=DataCleaned)
plt.title("Scatter plot Age vs Height")
plt.show()

################################################################################
# 9. LOG TRANSFORMATION OF AGE
################################################################################

DataCleaned['Log_Age'] = np.log(DataCleaned['Age'])
print(DataCleaned)

# 9.1 Scatter plot: Log Age vs Height
sns.scatterplot(x='Log_Age', y='Height_cm', data=DataCleaned)
plt.title("Scatter plot Log Age vs Height")
plt.show()

################################################################################
# 10. SIMPLE LINEAR REGRESSION: HEIGHT ~ LOG_AGE
################################################################################

X = sm.add_constant(DataCleaned['Log_Age'])
y = DataCleaned['Height_cm']
lm_r = sm.OLS(y, X).fit()
print(lm_r.summary())

################################################################################
# 11. ADD SALARY VARIABLE
################################################################################

DataCleaned['Salary'] = [35, 22, 55, 25, 23, 20, 40, 45, 25, 19, 41, 22]
print(DataCleaned)

################################################################################
# 12. CREATE BOOTSTRAP SAMPLES
################################################################################

bootstrap_samples = [
    DataCleaned.sample(n=len(DataCleaned), replace=True)
    for _ in range(1000)
]

################################################################################
# 13. BOOTSTRAPPING & LINEAR REGRESSION
################################################################################

boot_samples = 1000
boot_results = np.zeros((boot_samples, 2))
boot_data = []
boot_models = []

n = len(DataCleaned)

for i in range(boot_samples):
    samp_idx = np.random.choice(n, n, replace=True)
    boot_df = DataCleaned.iloc[samp_idx].copy()
    boot_data.append(boot_df)

    X = sm.add_constant(boot_df["Age"])
    y = boot_df["Salary"]
    
    model = sm.OLS(y, X).fit()
    boot_models.append(model)

    boot_results[i, :] = model.params.values

# 13.1 View first bootstrap regression model
first_model = boot_models[0]
print(first_model.summary())

################################################################################
# 14. MODEL EVALUATION: RMSE
################################################################################

coef_list = []
rmse_list = []
r2_list = []

for i in range(boot_samples):
    boot_data_i = DataCleaned.sample(n=n, replace=True)
    
    X = boot_data_i[['Age']]  # example with Age only
    X = sm.add_constant(X)
    y = boot_data_i['Salary']
    
    model = sm.OLS(y, X).fit()
    
    coef_list.append(model.params.values)
    
    y_pred = model.predict(X)
    rmse = np.sqrt(np.mean((y - y_pred)**2))
    rmse_list.append(rmse)
    
    r2_list.append(model.rsquared)

boot_results_df = pd.DataFrame(coef_list, columns=['Intercept', 'Age'])
boot_results_df['RMSE'] = rmse_list
boot_results_df['R2'] = r2_list

plt.hist(boot_results_df['RMSE'], bins=30, color='skyblue', edgecolor='black')
plt.axvline(x=np.mean(boot_results_df['RMSE']), color='red', linewidth=2)
plt.title('Bootstrap RMSE Distribution')
plt.xlabel('RMSE')
plt.ylabel('Frequency')
plt.show()

plt.hist(boot_results_df['R2'], bins=30, color='lightgreen', edgecolor='black')
plt.title('Bootstrap R² Distribution')
plt.xlabel('R²')
plt.ylabel('Frequency')
plt.show()

################################################################################
# End of Script
################################################################################

