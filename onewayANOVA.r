#Obtaining Data
CropData <-read.table("cropData.txt",header =TRUE,sep="\t", fill = TRUE)
head(CropData)

#Fitting the oneway model
one.way <- aov(yield ~ fertilizer, data = CropData)
