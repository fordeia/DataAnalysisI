#Loading packages
library(tidyverse)
library(readxl)

Data_to_clean<- read_excel("Data_Cleaning.xlsx")
head(Data_to_clean)

Summarizing the variables with count
Data_to_clean %>% count(Gender)
Data_to_clean %>% count(Age)
Data_to_clean %>% count(Status)

#Removing rows with impossible age values
Data_to_clean %>%
  filter(Age > 900)

Data_to_clean %>% count(Age)
