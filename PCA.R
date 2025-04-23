# Load libraries and data (replace with your data)
library(stats)
library(MASS)
# Example data
set.seed(123)
my_data <- data.frame(x1 = rnorm(100), x2 = rnorm(100), x3 = rnorm(100), outcome = rnorm(100))

# 1. PCA
pca_result <- prcomp(my_data[, 1:3], scale = TRUE, center = TRUE) # Don't include outcome in PCA

# 2. Analyze PCA results
summary(pca_result)

# 3. Select components (e.g., first two)
pca_data <- data.frame(pca_result$x)
selected_components <- pca_data[, 1:2]

# 4. Prepare data for MLR
regression_data <- data.frame(my_data$outcome, selected_components) # Combine outcome and PCs

# 5. Perform MLR
regression_model <- lm(my_data$outcome ~ ., data = regression_data)
summary(regression_model)
