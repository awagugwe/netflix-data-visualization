#R integration, implementing the most watched genres chart into R

#Load necessary libraries, png and grid 
library(png)
library(grid)

#Load images generated from Python
most_watched_genres_img<- readPNG("/Users/mac/Documents/4/genres_distribution.png")

#Display image of chart showing most watched genres on Netflix
grid.newpage()
grid.raster(most_watched_genres_img)


