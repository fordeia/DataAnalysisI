library(MASS)
immerData<-immer
head(immer)

#Writing to an excel file. 
library(openxlsx)
write.xlsx(immerData, 'C:/Users/fordeia/Desktop/immerData.xlsx')

# Wilcoxon signed rank test with continuity correction 
wilcox.test(immer$Y1, immer$Y2, paired=TRUE) 
