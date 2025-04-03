# Perform the two-way ANOVA
fit <- aov(yield ~ factor(fertilizer)*factor(density), data = CropData)

# Summarize the ANOVA results
summary(fit)

fit1 <- aov(yield ~ factor(fertilizer) + factor(density), data = CropData)

# Summarize the ANOVA results
summary(fit1)

# Post-hoc test (Tukey's HSD)

  TukeyHSD(fit1, conf.level=.95)
