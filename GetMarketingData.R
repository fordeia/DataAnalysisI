#Down loading the data
data("marketing", package = "datarium")
head(marketing)

#Writing to an excel file. 
library(openxlsx)
write.xlsx(marketing, './marketingData.xlsx')
