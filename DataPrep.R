#Loading packages
library(tidyverse)
library(readxl)

Data_to_clean<- read_excel("Data_Cleaning.xlsx")
Data_to_clean

Summarizing the variables with count
Data_to_clean %>% count(Gender)
Data_to_clean %>% count(Age)
Data_to_clean %>% count(Status)

#Removing rows with NA
Data_to_clean %>%
  na.omit()

#Remove rows with NA in specific colums
Data_to_clean %>%
  filter(!is.na(Gender))

#Removing rows with impossible age values
Data_to_clean %>%
  filter(Age < 900)

DataCleaned<-(Data_to_clean %>%
  filter(Age < 900))

DataCleaned
