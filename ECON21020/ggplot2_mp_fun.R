### ggplot2 practice on metrics project data

library(tidyverse)

combined <- merge(edu, f_edu, by="df$id")
combined <- merge(combined, birthyear, by="df$id")
names(combined) <- c("id", "edu", "f_edu", "birthyear")

combined <- combined[complete.cases(combined), ]
combined <- combined %>%
  mutate(group = case_when(
    birthyear < 1950 ~ "< 1950",
    birthyear >= 1950 & birthyear < 1960 ~ "1950-1959",
    birthyear >= 1960 & birthyear < 1970 ~ "1960-1969",
    birthyear >= 1970 & birthyear < 1980 ~ "1970-1979",
    birthyear >= 1980 & birthyear < 1990 ~ "1980-1989",
    birthyear > 1990 ~ "millenials"))

combined %>%
  filter(!is.na(group) & group != "millenials") %>%
    ggplot(aes(edu)) +
    geom_density() +
    facet_grid(group~.)

combined %>%
  filter(!is.na(group) & group != "millenials") %>%
    ggplot(aes(birthyear, edu)) +
    geom_jitter()

