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
plot.forecast(rainseriesforecasts2)



