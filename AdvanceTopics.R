########################################
# 1. Load Births Data
########################################
births <- scan("http://robjhyndman.com/tsdldata/data/nybirths.dat")
birthstimeseries <- ts(births, frequency=12, start=c(1946,1))
birthstimeseries

########################################
# 2. Plot Births Time Series
########################################
plot.ts(birthstimeseries)

########################################
# 3. Load Kings Data
########################################
kings <- scan("http://robjhyndman.com/tsdldata/misc/kings.dat", skip=3)
kingstimeseries <- ts(kings)
plot.ts(kingstimeseries)

########################################
# 4. Moving Average Smoothing (Order 3)
########################################
install.packages("TTR")
library("TTR")
kingstimeseriesSMA3 <- SMA(kingstimeseries, n=3)
plot.ts(kingstimeseriesSMA3)

########################################
# 5. Moving Average Smoothing (Order 8)
########################################
kingstimeseriesSMA8 <- SMA(kingstimeseries, n=8)
plot.ts(kingstimeseriesSMA8)

########################################
# 6. Decompose Births Time Series
########################################
birthstimeseriescomponents <- decompose(birthstimeseries)

########################################
# 7. Output Seasonal, Trend, Random Components
########################################
birthstimeseriescomponents$seasonal
birthstimeseriescomponents$trend
birthstimeseriescomponents$random

########################################
# 8. Plot Time-Series Components
########################################
plot(birthstimeseriescomponents)

########################################
# 9. Seasonal Adjustment
########################################
birthstimeseriescomponents <- decompose(birthstimeseries)
birthstimeseriesseasonallyadjusted <- birthstimeseries - birthstimeseriescomponents$seasonal

########################################
# 10. Plot Seasonally Adjusted Series
########################################
plot(birthstimeseriesseasonallyadjusted)

########################################
# 11. Load Rainfall Data
########################################
rain <- scan("http://robjhyndman.com/tsdldata/hurst/precip1.dat", skip=1)
rainseries <- ts(rain, start=c(1813))
rainseries

########################################
# 12. Plot Rainfall Time Series
########################################
plot.ts(rainseries)

########################################
# 13. Simple Exponential Smoothing
########################################
rainseriesforecasts <- HoltWinters(rainseries, beta=FALSE, gamma=FALSE)
rainseriesforecasts

########################################
# 14. Fitted Values from Smoothing
########################################
rainseriesforecasts$fitted

########################################
# 15. Plot Holt-Winters Model Fit
########################################
plot(rainseriesforecasts)

########################################
# 16. SSE for Forecast Accuracy
########################################
rainseriesforecasts$SSE

########################################
# 17. Simple Exponential Smoothing With Initial Level
########################################
HoltWinters(rainseries, beta=FALSE, gamma=FALSE, l.start=23.56)

########################################
# 18. Forecast Future Values
########################################
install.packages("forecast")
library("forecast")
rainseriesforecasts2 <- forecast(rainseriesforecasts, h=8)
rainseriesforecasts2

########################################
# 19. Plot Forecasted Values
########################################
plot(rainseriesforecasts2)

########################################
# 20. Correlogram of Residuals
########################################
acf(rainseriesforecasts2$residuals, na.action = na.pass, lag.max=20)

########################################
# 21. Ljung–Box Test for Residual Autocorrelation
########################################
Box.test(rainseriesforecasts2$residuals, lag=20, type="Ljung-Box")

##################################################
############ Principal Component Analysis #########
##################################################

########################################
# 22. Load Example PCA Data
########################################
library(stats)
library(MASS)
set.seed(123)
my_data <- data.frame(
  x1 = rnorm(100),
  x2 = rnorm(100),
  x3 = rnorm(100),
  outcome = rnorm(100)
)

########################################
# 23. Perform PCA
########################################
pca_result <- prcomp(my_data[, 1:3], scale = TRUE, center = TRUE)

########################################
# 24. PCA Summary
########################################
summary(pca_result)

########################################
# 25. Display Loadings
########################################
pca_result

########################################
# 26. Select First Two PCs
########################################
pca_data <- data.frame(pca_result$x)
selected_components <- pca_data[, 1:2]
head(selected_components)

########################################
# 27. Scree Plot
########################################
install.packages("factoextra")
library(factoextra)
fviz_eig(pca_result, addlabels = TRUE)

########################################
# 28. PCA Variable Biplot
########################################
fviz_pca_var(pca_result, col.var = "black")

########################################
# 29. Prepare Data for Regression
########################################
regression_data <- data.frame(my_data$outcome, selected_components)

########################################
# 30. Multiple Linear Regression Using PCs
########################################**
regression_model <- lm(my_data$outcome ~ PC1 + PC2, data = regression_data)
summary(regression_model)

##################################################
############ PCA Assignment: Iris Dataset #########
##################################################

########################################
# 31. Load Iris Data
########################################
data("iris")
str(iris)
head(iris)

########################################
# 32. Perform PCA on Iris
########################################
pc <- prcomp(iris[,-5], center = TRUE, scale. = TRUE)
summary(pc)
pc

########################################
# 33. Iris Scree Plot
########################################
fviz_eig(pc, addlabels = TRUE)

########################################
# 34. Iris PCA Variable Plot
########################################
fviz_pca_var(pc, col.var = "black")
