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

# Prepare data for MLR
regression_data <- data.frame(mtcars$mpg, X_pca) # Combine outcome and PCs

# Perform MLR with PC
regression_model <- lm(mtcars$mpg ~PC1 + PC2 + PC3 + PC4 + PC5 + PC6, data = regression_data)
summary(regression_model)

#Question 4 ===========================================
#Rainfall data
rain <- scan("http://robjhyndman.com/tsdldata/hurst/precip1.dat",skip=1)
#Read 100 items
rainseries <- ts(rain,start=c(1813))
rainseries

#plot
plot.ts(rainseries)

#Simple Exponential Smoothing
rainseriesforecasts <- HoltWinters(rainseries, beta=FALSE, gamma=FALSE)
rainseriesforecasts

#The forcasted time series
head(rainseriesforecasts$fitted)

#Plot
plot(rainseriesforecasts)

#Sum of square error to estimate accuracy of the forecast. 
rainseriesforecasts$SSE

#Simple Exponential Smoothing using the initial value of the time series
HoltWinters(rainseries, beta=FALSE, gamma=FALSE, l.start=23.56)

#Forcasting for time periods outside of the time series
install.packages("forecast")
library("forecast")

rainseriesforecasts2 <- forecast(rainseriesforecasts, h=8)
rainseriesforecasts2

#Plotting prediction for the forecast
plot(rainseriesforecasts2)

#Correlogram to test for auto-correlation
acf(rainseriesforecasts2$residuals, na.action = na.pass, lag.max=20)

#Box test to test for auto-correlation
Box.test(rainseriesforecasts2$residuals, lag=20, type="Ljung-Box")



