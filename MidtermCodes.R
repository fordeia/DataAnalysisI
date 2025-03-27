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
 #calculate max length of vectors
max_length <- max(length(Men_bodyfat), length(Women_bodyfat))

#set length of each vector equal to max length
length(Men_bodyfat) <- max_length                      
length(Women_bodyfat) <- max_length

bodyfat_data=cbind(Men_bodyfat,Women_bodyfat) 
bodyfat_data
  
# boxplot 
boxplot(bodyfat_data,beside=T) 

# Shapiro-Wilk normality test for Men's body fat
shapiro.test(Men_bodyfat)

# Shapiro-Wilk normality test for Women's body fat
shapiro.test(Women_bodyfat)

#Equal variance test
var.test(Men_bodyfat, Women_bodyfat)

#Two sample t-test
t.test(Men_bodyfat, Women_bodyfat, var.equal = TRUE)
