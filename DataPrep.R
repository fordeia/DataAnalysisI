#Loading packages
library(tidyverse)
library(readxl)

Data_to_clean<- read_excel("Data_Cleaning.xlsx")

Summarizing the variables with count
Data_to_clean %>% count(Gender)
Data_to_clean %>% count(Age)
Data_to_clean %>% count(Status)
