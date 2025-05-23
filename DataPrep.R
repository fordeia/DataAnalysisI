-#Loading packages
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
DataCleaned$Salary<- c(35,22, 55, 25, 23, 20,40, 45, 25, 19, 41) 
print(DataCleaned)

#Creating a bootstrap sample from the cleaned data
bootDataCleaned=DataCleaned[sample(nrow(DataCleaned), 1000, replace=TRUE), ]

#Machine Learning (Assume all assumptions are met)######################################################################
# Bootstrapping
boot_samples <- 1000  # Number of bootstrap samples
boot_results <- matrix(0, nrow = boot_samples, ncol = 2 )

# Fit MLR models to bootstrap samples
# create an empty list to store the samples
boot_data <- list()

for (i in 1:boot_samples) {
  # Bootstrap sample
  samp<-sample(nrow(DataCleaned), replace = TRUE)
  boot_data[[i]]<-DataCleaned[samp,]
  
  # Fit MLR model using selected variables
  mlr_model <- lm(Salary~ Age, data = boot_data[[i]])
  
 # Store coefficient estimates
  boot_results[i, ] <- coef(mlr_model)

}
# view the first sample
head(boot_data[[1]])

#Evaluating the model

OrigDataSel<-DataCleaned[,3]

Pred<-matrix(0,nrow(boot_results),nrow(OrigDataSel))

for (i in 1:nrow(boot_results)) {
   for (j in 1:nrow(OrigDataSel)) {
        Pred[[i,j]]<-sum(boot_results[i,1]+boot_results[i,2]*OrigDataSel[j,1])
    }
}

Act<-matrix(0,nrow(boot_results),nrow(DataCleaned))

for (i in 1:nrow(boot_results)) {
   for (j in 1:nrow(DataCleaned)) {  
      Act[[i,j]]<-unlist(DataCleaned[j,7])
  }
}

residuals<-Act-Pred
ErrSq<-residuals^2

SSE<- rowSums(ErrSq)

MSE<-SSE/nrow(DataCleaned)

RMSE<-sqrt(MSE)
hist(RMSE)

shapiro.test(RMSE)








