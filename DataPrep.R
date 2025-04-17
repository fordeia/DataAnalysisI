#Loading packages
library(tidyverse)
library(readxl)
library(forcats)
library(dplyr)


Data_to_clean<- read_excel("Data_Cleaning.xlsx")
Data_to_clean

Summarizing the variables with count
Data_to_clean %>% count(Gender)
Data_to_clean %>% count(Age)
Data_to_clean %>% count(Status)

######workflow######
#Reloading data
Data_to_clean<- read_excel("Data_Cleaning.xlsx")

#Remove rows with NA in specific colums
DataCleaned<-(Data_to_clean %>%
  filter(!is.na(Status)))

DataCleaned<-(DataCleaned %>%
  distinct())

#Renaming levels
DataCleaned$Gender <- fct_recode(DataCleaned$Gender, "female" = "Female", "female" ="femail")

DataCleaned$Age<-na_if(DataCleaned$Age, 999)

DataCleaned

  # Impute with the mean
        DataCleaned <- DataCleaned %>% 
          mutate(Age = replace_na(Age, round(mean(Age, na.rm = TRUE))))
        # Or, impute with the median
        DataCleaned <- DataCleaned %>%
          mutate(Age = replace_na(Age, median(Age, na.rm = TRUE)))

print(DataCleaned)

#Boxplot
p <- ggplot(DataCleaned, aes(Gender, Age))
p + geom_boxplot() + ggtitle("Comparative Boxplot Gender vs Age")


#Adding a height variable
DataCleaned$Height_cm <- c(160, 175, 155, 165, 178, 190, 191, 180, 159, 167, 167) 
print(DataCleaned)


# basic scatterplot
ggplot(DataCleaned, aes(x=Age, y=Height_cm)) + 
    geom_point() + ggtitle("Scatter plot Age vs Height")

#Log transformation of data
DataCleaned$Log_Age<-log(DataCleaned$Age)
print(DataCleaned)

#Scatter plot log age versus height
# basic scatterplot
ggplot(DataCleaned, aes(x=Log_Age, y=Height_cm)) + 
    geom_point() + ggtitle("Scatter plot Log Age vs Height")

# Fitting Simple Linear Regression 
lm.r= lm(formula = Height_cm ~ Log_Age,
         data = DataCleaned)
#Summary of the model
summary(lm.r)

#Adding a salary variable
DataCleaned$Salary_$ <- c(35,22, 55, 25, 23, 20,40, 45, 25, 19, 41) 
print(DataCleaned)

#Creating a bootstrap sample from the cleaned data
bootDataCleaned=DataCleaned[sample(nrow(DataCleaned), 1000, replace=TRUE), ]

#Machine Learning (Assume all assumptions are met)
#Splitting the data 70:30 
set.seed(25)
samp <- sample(nrow(bootDataCleaned), 0.7 * nrow(bootDataCleaned))
train <- bootDataCleaned[samp, ]
test <- bootDataCleaned[-samp, ]

#Training the model
# Fit the model and obtain summary
model <- lm(Salary_$ ~ Age, data = train)
summary(model)

# Make predictions on the test set
predictions <- predict(model, test)

# Put height and prediction in a dataframe
eval <- cbind(test$Salary_$, predictions)
colnames(eval) <- c("Y", "Yhat")
eval <- as.data.frame(eval)
head(eval)

# Evaluate model performance with root mean square error
mse <- mean((eval$Y - eval$Yhat)^2)
rmse <- sqrt(mse)
rmse

#Evaluated model performance with observed vs predictive plots


ggplot(test, aes(x = Height_cm, y = predictions )) +
  geom_point() +
  geom_abline(intercept = 0, slope = 1, color = "red") +
  xlab("Observed Values") +
  ylab("Predicted Values") +
  ggtitle("Observed vs. Predicted Values")

#Evaluating model performance with R-squared. 
str(summary(model))








