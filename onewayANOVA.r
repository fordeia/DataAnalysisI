#Obtaining Data
CropData <-read.table("cropData.txt",header =TRUE,sep="\t", fill = TRUE)
head(CropData, 10)

#Fitting the oneway model
one.way <- aov(yield ~ fertilizer, data = CropData)
summary(one.way)

#Table of fertilizer data
table(CropData$fertilizer)

#Tukey HSD test to see which groups as statistically significantly different. 
TukeyHSD(one.way, conf.level=.95)

