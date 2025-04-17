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

#Creating a bootstrap sample from the cleaned data
bootDataCleaned=DataCleaned[sample(nrow(DataCleaned), 1000, replace=TRUE), ]





