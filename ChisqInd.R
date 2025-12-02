#Recreating the contingency table in R:

Contingtable = matrix(c(50,125,90,45,75,175,30,10),ncol=2) 
colnames(Contingtable) = c("Snacks","No Snacks") 
rownames(Contingtable) = c("Action","Comedy","Family", "Horror")
print(Contingtable)

#Visualizing the data with a balloonplot
install.packages("gplots")
library("gplots") 
#convert the data as a table 
dt <- as.table(as.matrix(Contingtable)) 
#Graph 
balloonplot(t(dt), main ="Purchase", xlab ="", ylab="", label = FALSE, show.margins = FALSE) 

#Chi-square test
chisq<-chisq.test(Contingtable) 
chisq

#Expected values 
chisq$expected



