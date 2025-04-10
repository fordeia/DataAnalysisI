options(scipen = 999)
#Obtaining Data
CropData <-read.table("cropData.txt",header =TRUE,sep="\t", fill = TRUE)
head(CropData, 10)

boxplot(CropData$yield ~ CropData$fertilizer)

#Fitting the oneway model
one.way <- aov(yield ~ factor(fertilizer), data = CropData)
summary(one.way)

#Table of fertilizer data
table(CropData$fertilizer)

#Tukey HSD test to see which groups as statistically significantly different. 
TukeyHSD(one.way, conf.level=.95)

#With blocking
one.wayBlocking <- aov(yield ~ block + factor(fertilizer), data = CropData)
summary(one.wayBlocking)




