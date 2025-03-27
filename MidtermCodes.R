#Two sample t test
Men_bodyfat <- c(13.3,6,20,8,14,19,18,25,16,24,15,1,15)
Women_bodyfat <- c(22,16,21.7,21,30,12,23.2,28,23)

t.test(Men_bodyfat, Women_bodyfat, var.equal = TRUE)
