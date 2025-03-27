#Two sample t test
Men_bodyfat <- c(13.3,6,20,8,14,19,18,25,16,24,15,1,15)
Women_bodyfat <- c(22,16,21.7,21,30,12,23.2,28,23)

#Count, mean and standard deviation
#Men 
length(Men_bodyfat) 
mean(Men_bodyfat) 
sd(Men_bodyfat) 
#Women
length(Women_bodyfat) 
mean(Women_bodyfat) 
sd(Women_bodyfat) 

# combine two vectors using cbind 
  if (nrow(Men_bodyfat) < nrow(Women_bodyfat)) {
        # Pad Men_bodyfat with NA rows
        Men_bodyfat <- rbind(Men_bodyfat, matrix(NA, nrow = nrow(Women_bodyfat) - nrow(Men_bodyfat), ncol = ncol(Men_bodyfat)))
    } else if (nrow(Women_bodyfat) < nrow(Men_bodyfat)) {
        # Pad Women_bodyfat with NA rows
        Women_bodyfat <- rbind(Women_bodyfat, matrix(NA, nrow = nrow(Men_bodyfat) - nrow(Women_bodyfat), ncol = ncol(Women_bodyfat)))
    }
bodyfat_data=cbind(Men_bodyfat,Women_bodyfat) 
  
# boxplot 
boxplot(bodyfat_data,beside=T) 

#Two sample t-test
t.test(Men_bodyfat, Women_bodyfat, var.equal = TRUE)
