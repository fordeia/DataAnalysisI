#Recreating the contingency table in R:

Contintable=matrix(c(50,125,90,45,75,175,30,10),ncol=2) 
colnames(Contintable)=c("Snacks","No Snacks") 
rownames(Contintable)=c("Action","Comedy","Family", "Horror")
print(Contintable)

#Visualizing the data with a balloonplot
install.packages("gplots")
library("gplots") 
#convert the data as a table 
dt <- as.table(as.matrix(Contintable)) 
#Graph 
balloonplot(t(dt), main ="Purchase", xlab ="", ylab="", label = FALSE, show.margins = FALSE) 

#Chi-square test
chisq<-chisq.test(Contintable) 
chisq

#Expected values 
chisq$expected


