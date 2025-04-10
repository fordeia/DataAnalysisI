library(MASS)
head(immer)

# Wilcoxon signed rank test with continuity correction 
wilcox.test(immer$Y1, immer$Y2, paired=TRUE) 
