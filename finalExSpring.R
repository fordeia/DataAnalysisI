#Question 3 ==============================
#Down loading the mtcars dataset
data("mtcars")
head(mtcars)

#The principal component analysis
library(stats)
pca_result <- prcomp(mtcars[, -1], scale = TRUE, center = TRUE) # Don't include outcome in PCA
summary(pca_result)

#Display the loading with respect to the independent varialbes
pca_result

