################################################################################
# 1. LOAD REQUIRED PACKAGES
################################################################################

library(tidyverse)
library(readxl)
library(forcats)
library(dplyr)


################################################################################
# 2. IMPORT DATA
################################################################################

Data_to_clean <- read_excel("Data_Cleaning.xlsx")
Data_to_clean


################################################################################
# 3. SUMMARIZE VARIABLES WITH COUNT
################################################################################

Data_to_clean %>% count(Gender)
Data_to_clean %>% count(Age)
Data_to_clean %>% count(Status)


################################################################################
# 4. DATA CLEANING WORKFLOW
################################################################################

# Reload data
Data_to_clean <- read_excel("Data_Cleaning.xlsx")

# Remove rows with missing Status
DataCleaned <- Data_to_clean %>%
  filter(!is.na(Status))

# Remove duplicate rows
DataCleaned <- DataCleaned %>%
  distinct()

# Rename / correct gender levels
DataCleaned$Gender <- fct_recode(DataCleaned$Gender,
                                 "female" = "Female",
                                 "female" = "femail")

# Replace placeholder values (999) with NA in Age
DataCleaned$Age <- na_if(DataCleaned$Age, 999)

# View intermediate cleaned dataset
DataCleaned


################################################################################
# 5. HANDLE MISSING VALUES BY IMPUTATION
################################################################################

# Impute with mean
DataCleaned <- DataCleaned %>%
  mutate(Age = replace_na(Age, round(mean(Age, na.rm = TRUE))))

# Or impute with median
DataCleaned <- DataCleaned %>%
  mutate(Age = replace_na(Age, median(Age, na.rm = TRUE)))

# View final cleaned dataset
print(DataCleaned)


################################################################################
# 6. VISUALIZATION: COMPARATIVE BOX PLOT
################################################################################

p <- ggplot(DataCleaned, aes(Gender, Age))
p + geom_boxplot() + ggtitle("Comparative Boxplot: Gender vs Age")


################################################################################
# 7. ADDING A NEW VARIABLE (HEIGHT)
################################################################################

DataCleaned$Height_cm <- c(160, 175, 155, 165, 178, 190, 191, 180, 159, 167, 167, 159)
print(DataCleaned)


################################################################################
# 8. SCATTER PLOT: AGE VS HEIGHT
################################################################################

ggplot(DataCleaned, aes(x = Age, y = Height_cm)) +
  geom_point() +
  ggtitle("Scatter Plot: Age vs Height")


################################################################################
# 9. LOG TRANSFORMATION OF AGE
################################################################################

DataCleaned$Log_Age <- log(DataCleaned$Age)
print(DataCleaned)

# Scatter plot: Log Age vs Height
ggplot(DataCleaned, aes(x = Log_Age, y = Height_cm)) +
  geom_point() +
  ggtitle("Scatter Plot: Log(Age) vs Height")


################################################################################
# 10. SIMPLE LINEAR REGRESSION: HEIGHT ~ LOG(AGE)
################################################################################

lm.r <- lm(formula = Height_cm ~ Log_Age, data = DataCleaned)

# Display summary
summary(lm.r)


################################################################################
# 11. ADDING A SALARY VARIABLE
################################################################################

DataCleaned$Salary <- c(35, 22, 55, 25, 23, 20, 40, 45, 25, 19, 41)
print(DataCleaned)


################################################################################
# 12. CREATE A BOOTSTRAP SAMPLE
################################################################################

set.seed(123)  # for reproducibility

bootstrap_samples <- lapply(1:1000, function(i) {
  DataCleaned[sample(nrow(DataCleaned), nrow(DataCleaned), replace = TRUE), ]
})


################################################################################
# 13. BOOTSTRAPPING & LINEAR REGRESSION
################################################################################

boot_samples <- 1000  # Number of bootstrap samples
boot_results <- matrix(0, nrow = boot_samples, ncol = 2)

# Empty list to store bootstrap datasets
boot_data <- vector("list", boot_samples)

# Empty list to store models if you want them
boot_models <- vector("list", boot_samples)

for (i in 1:boot_samples) {
  
  # Bootstrap sample (same number of rows as original)
  samp <- sample(nrow(DataCleaned), nrow(DataCleaned), replace = TRUE)
  
  boot_data[[i]] <- DataCleaned[samp, ]
  
  # Fit MLR model (Salary ~ Age)
  mlr_model <- lm(Salary ~ Age, data = boot_data[[i]])
  
  # Store the model
  boot_models[[i]] <- mlr_model
  
  # Store coefficients (intercept + slope)
  boot_results[i, ] <- coef(mlr_model)
}

# =========================================
# 🔍 View the first bootstrap regression model
# =========================================
first_model <- boot_models[[1]]
summary(first_model)



################################################################################
# 14. MODEL EVALUATION
################################################################################

# Original predictor (Age, assuming column 3)
OrigDataSel <- DataCleaned[, 3]  

# Prepare matrices
n_boot <- nrow(boot_results)
n_obs <- nrow(DataCleaned)
Pred <- matrix(0, nrow = n_boot, ncol = n_obs)

# Compute predictions for each bootstrap model
for (i in 1:n_boot) {
  Pred[i, ] <- boot_results[i, 1] + boot_results[i, 2] * OrigDataSel
}

# Actual outcomes (Salary, assuming column 7)
Act <- matrix(rep(DataCleaned[, 7], each = n_boot), nrow = n_boot)

# Residuals
residuals <- Act - Pred

# RMSE for each bootstrap
RMSE <- sqrt(rowMeans(residuals^2))

# Visualize RMSE distribution
hist(RMSE, main = "Histogram of RMSE (Bootstrap)", col = "skyblue", border = "black")

# Normality test for RMSE
shapiro.test(RMSE)

################################################################################
# END OF SCRIPT
################################################################################








