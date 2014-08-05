#! /usr/bin/Rscript

library(ggplot2)

df <- read.csv('data.csv')
options(device="png")

ggplot(df, aes(x=assembly_id, y=nbills, fill=nbills)) +
  geom_bar(stat="identity") +
  geom_text(label=df$nbills, vjust=-0.4, size=4)

ggplot(df, aes(x=assembly_id, y=bills_per_year, fill=bills_per_year)) +
  geom_bar(stat="identity") +
  geom_text(label=round(df$bills_per_year), vjust=-0.4, size=4)
