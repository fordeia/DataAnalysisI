CBloom <-read.table("cherry_blossom.txt",header =TRUE,sep="\t", fill = TRUE)

# Create a new variable by summing two existing variables
    my_data$sum_col <- my_data$col1 + my_data$col2
