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

DataCleaned$Height_cm <- c(160, 175, 155, 165, 178, 190, 191, 180, 159, 167, 167, 187)
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

bootDataCleaned <- DataCleaned[sample(nrow(DataCleaned), 1000, replace = TRUE), ]


################################################################################
# 13. BOOTSTRAPPING & MULTIPLE LINEAR REGRESSION
################################################################################

boot_samples <- 1000  # Number of bootstrap samples
boot_results <- matrix(0, nrow = boot_samples, ncol = 2)

# Empty list to store bootstrap samples
boot_data <- list()

for (i in 1:boot_samples) {
  
  # Bootstrap sample
  samp <- sample(nrow(DataCleaned), replace = TRUE)
  boot_data[[i]] <- DataCleaned[samp, ]
  
  # Fit MLR model (Salary ~ Age)
  mlr_model <- lm(Salary ~ Age, data = boot_data[[i]])
  
  # Store coefficients
  boot_results[i, ] <- coef(mlr_model)
}

# View first bootstrap sample
head(boot_data[[1]])


################################################################################
# 14. MODEL EVALUATION
################################################################################

OrigDataSel <- DataCleaned[, 3]

Pred <- matrix(0, nrow(boot_results), nrow(OrigDataSel))

for (i in 1:nrow(boot_results)) {
  for (j in 1:nrow(OrigDataSel)) {
    Pred[[i, j]] <- sum(boot_results[i, 1] + boot_results[i, 2] * OrigDataSel[j, 1])
  }
}

Act <- matrix(0, nrow(boot_results), nrow(DataCleaned))

for (i in 1:nrow(boot_results)) {
  for (j in 1:nrow(DataCleaned)) {
    Act[[i, j]] <- unlist(DataCleaned[j, 7])
  }
}

residuals <- Act - Pred
ErrSq <- residuals^2
SSE <- rowSums(ErrSq)
MSE <- SSE / nrow(DataCleaned)
RMSE <- sqrt(MSE)

# Visualize RMSE distribution
hist(RMSE, main = "Histogram of RMSE (Bootstrap)", col = "skyblue", border = "black")

# Normality test for RMSE
shapiro.test(RMSE)

################################################################################
# END OF SCRIPT
################################################################################


