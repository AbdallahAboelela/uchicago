# List of files to download
file_names <- list.files(path="/Users/abdallahaboelela/Desktop/metrics_project/mp_data", full.names=TRUE)
df <- data.frame()

require(dplyr)
for (file_name in file_names) {
  temp <- read.csv(file=file_name, header=T)
  df <- bind_rows(df, temp)
}

avg_f_inc_labor <- aggregate(df$f_inc_labor ~ df$id, data=df, FUN=mean)
avg_m_inc_labor <- aggregate(df$m_inc_labor ~ df$id, data=df, FUN=mean)
edu <- aggregate(df$edu ~ df$id, data = df, FUN=max)
f_edu <- aggregate(df$f_edu ~ df$id, data = df, FUN=max)
m_edu <- aggregate(df$m_edu ~ df$id, data = df, FUN=max)
birthyear <- aggregate(df$birthyear ~ df$id, data = df, FUN=min)
male <- aggregate(df$male ~ df$id, data = df, FUN=max)

combined <- merge(avg_f_inc_labor, avg_m_inc_labor, by="df$id")
combined <- merge(combined, edu, by="df$id")
combined <- merge(combined, f_edu, by="df$id")
combined <- merge(combined, m_edu, by="df$id")
combined <- merge(combined, birthyear, by="df$id")
combined <- merge(combined, male, by="df$id")
colnames(combined) <- c("id", "avg_f_labor", "avg_m_labor", "edu", "f_edu", "m_edu", "birthyear", "male")

combined$p_labor_inc <- combined$avg_f_labor + combined$avg_m_labor

df.age <- combined[combined$birthyear <= 1988 & combined$birthyear > 1983, ]

fit <- lm(edu ~ m_edu * male + f_edu * male + p_labor_inc, data = df.age)
summary(fit)