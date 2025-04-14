#Loading packages
library(tidyverse)
library(readxl)

Data_to_clean<- read_excel("Data_Cleaning.xlsx")

Summarizing the variables with count
Data_to_clean %>% count(Gender)
