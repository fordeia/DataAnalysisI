#Installing and unloading packages
install.packages("pacman")
library(pacman)
library(tidyverse)

#Importing the data
retail <- read_csv("https://raw.githubusercontent.com/PacktPublishing/Forecasting-Time-Series-Data-with-Facebook-Prophet/main/data/online_retail.csv")

#Ploting the time series 
retailtimeseries <- ts(retail)
plot.ts(retailtimeseries)

#Smoothing using a moving average of 3
install.packages("TTR")
library("TTR")
retailtimeseriesSMA3 <- SMA(retailtimeseries,n=3)
plot.ts(retailtimeseriesSMA3)
