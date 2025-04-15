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

DataCleaned
