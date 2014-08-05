#! /usr/bin/Rscript

library('timeline')

df <- read.csv('data.csv')
df$assembly_id <- as.character(df$assembly_id)
df$start_date <- as.Date(df$start_date)
df$end_date <- as.Date(df$end_date)
str(df)

png('drawing.png', width=1600, height=400)
timeline(df, text.angle=90, text.position='center', col=rainbow(12))
