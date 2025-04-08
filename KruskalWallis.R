#Importing data
PlantGrowth<-PlantGrowth
head(PlantGrowth)

#Displaying group levels
levels(PlantGrowth$group)

PlantGrowth$group <- ordered(PlantGrowth$group,levels = c("ctrl", "trt1", "trt2"))
