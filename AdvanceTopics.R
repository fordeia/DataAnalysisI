births <- scan("http://robjhyndman.com/tsdldata/data/nybirths.dat")
birthstimeseries <- ts(births, frequency=12, start=c(1946,1))
birthstimeseries

#Plotting the timeseries
plot.ts(birthstimeseries)

#The kings time series
kings <- scan("http://robjhyndman.com/tsdldata/misc/kings.dat",skip=3)
kingstimeseries <- ts(kings)
plot.ts(kingstimeseries)

#Smoothing the kings data, it is non-seasonal and the fluctuation are roughly the same size hence could be described by a additive model

#Smoothing using a moving average of 3
install.packages("TTR")
library("TTR")
kingstimeseriesSMA3 <- SMA(kingstimeseries,n=3)
plot.ts(kingstimeseriesSMA3)

#Smoothing order 8
kingstimeseriesSMA8 <- SMA(kingstimeseries,n=8)
plot.ts(kingstimeseriesSMA8)

#To estimate the trend, seasonal and irregular components of this time series, we type:
birthstimeseriescomponents <- decompose(birthstimeseries)

#Outputing the individual components
birthstimeseriescomponents$seasonal
birthstimeseriescomponents$trend
birthstimeseriescomponents$random

#Plotting the components
plot(birthstimeseriescomponents)

#Seasonal adjustment
birthstimeseriescomponents <- decompose(birthstimeseries)
birthstimeseriesseasonallyadjusted <- birthstimeseries - birthstimeseriescomponents$seasonal

#Ploting the adjusted time series
plot(birthstimeseriesseasonallyadjusted)

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
rainseriesforecasts$fitted

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
acf(x, na.action = na.pass)
acf(rainseriesforecasts2$residuals, lag.max=20)

#Box test to test for auto-correlation
Box.test(rainseriesforecasts2$residuals, lag=20, type="Ljung-Box")



#######Principal Component Analysis########

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




