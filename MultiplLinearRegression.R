library(tidyverse)
#Down loading the data
data("marketing", package = "datarium")
head(marketing)

#Fitting the model
model <- lm(sales ~ youtube + facebook + newspaper, data = marketing)
summary(model)

#Removing the insignificant variable and refitting the model
model  <- lm(sales ~ youtube + facebook, data = marketing)
summary(model)
