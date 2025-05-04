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

#Scree plot
install.packages("factoextra")
library(factoextra)
fviz_eig(pca_result, addlabels = TRUE)

#Biplot to display the relationship between the PC and independent variables. 
fviz_pca_var(pca_result, col.var = "black")

#Extracting components that explains 95% of the variability
explained_variance <- pca_result$sdev^2 / sum(pca_result$sdev^2)
cumulative_variance <- cumsum(explained_variance)
n_components <- which(cumulative_variance >= 0.95)[1] # Keep until 95% explained variance
X_pca <- as.data.frame(pca_result$x[, 1:n_components])
head(X_pca)

