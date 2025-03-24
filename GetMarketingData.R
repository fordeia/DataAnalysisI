#Down loading the data
data("marketing", package = "datarium")
head(marketing)

#Writing to an excel file. 
write.xlsx(marketing, 'C:/Users/fordeia/DataAnalysisI/marketingData.xlsx')
