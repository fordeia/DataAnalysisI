#Mann-Whitney U Test
x<-c(540,670,1000,960,1200,4650,4200)
y<-c(5000,4200,1300,900,7400,4500,7500)
wilcox.test(x, y, alternative = "two.sided", exact = TRUE)
