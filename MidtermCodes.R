# Testing the normality assumption, Q-Q plot
# read in the data
x <- c(28,29,35,37,32,26,37,39,22,29,36,38)
# making the qqplot
qqnorm(x)
qqline(x)

#One sample t-test
x <- c(28,29,35,37,32,26,37,39,22,29,36,38)
t.test(x, mu = 28, alternative = "two.sided")

#Two samples
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

#Two sample Welch's t-test
t.test(Men_bodyfat, Women_bodyfat, var.equal = FALSE)

#Loading heart data
heart_data <-read.table("heart_data.txt",header =TRUE,sep="\t", fill = TRUE)
head(heart_data)

model <- lm(heart.disease ~ biking + smoking, data = heart_data)
summary(model)

#Use a residual plot to test the linearity and homoskedasticity (equal variance) assumptions.
plot(model, which=1)

#Use a normal probability plot to test the normality assumption.
plot(model, which=2)

#Testing the normality assumption using a histogram
hist(residuals(model))

#Shapiro-Wilk test for normality
shapiro.test(residuals(model))

#Use the variance inflated factor to test for multicollinearity. 
library(usdm)
library(car)
vif(model)


