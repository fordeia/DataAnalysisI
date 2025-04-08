#Installing the packages
install.packages("ggpubr")
library("ggpubr")

#Importing data
PlantGrowth<-PlantGrowth
head(PlantGrowth)

#Displaying group levels
levels(PlantGrowth$group)

#Reording levels
PlantGrowth$group <- ordered(PlantGrowth$group,levels = c("ctrl", "trt1", "trt2"))

#Loading the dplyr 
library(dplyr)

#Computing the summary statistics
group_by(PlantGrowth, group) %>%
  summarise(
    count = n(),
    mean = mean(weight, na.rm = TRUE),
    sd = sd(weight, na.rm = TRUE),
    median = median(weight, na.rm = TRUE),
    IQR = IQR(weight, na.rm = TRUE)
  )

#Visualizing the data
#Boxplots
ggboxplot(my_data, x = "group", y = "weight",
          color = "group", palette = c("#00AFBB", "#E7B800", "#FC4E07"),
          order = c("ctrl", "trt1", "trt2"),
          ylab = "Weight", xlab = "Treatment")
