# 1. Install and load necessary libraries
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(patchwork)) install.packages("patchwork") # For combining plots

library(ggplot2)
library(patchwork)

# 2. Generate Sample Data
set.seed(42)
data <- data.frame(
  Group = rep(c("Alpha", "Beta", "Gamma"), each = 100),
  Value = c(rnorm(100, 10, 2), rnorm(100, 12, 4), rnorm(100, 11, 1.5))
)

# 3. Create different visualization styles
# Style A: Standard Boxplot
p1 <- ggplot(data, aes(x = Group, y = Value, fill = Group)) +
  geom_boxplot() +
  labs(title = "1. Standard", subtitle = "Classic quartiles & outliers") +
  theme_minimal() +
  theme(legend.position = "none")

p1
# Style B: Notched Boxplot
p2 <- ggplot(data, aes(x = Group, y = Value, fill = Group)) +
  geom_boxplot(notch = TRUE) +
  labs(title = "2. Notched", subtitle = "Confidence intervals for medians") +
  theme_minimal() +
  theme(legend.position = "none")

p2

# Style C: Boxplot with Jittered Points
p3 <- ggplot(data, aes(x = Group, y = Value, fill = Group)) +
  geom_boxplot(outlier.shape = NA, alpha = 0.7) +
  geom_jitter(width = 0.2, alpha = 0.4, size = 1) +
  labs(title = "3. With Jitter", subtitle = "Shows raw data distribution") +
  theme_minimal() +
  theme(legend.position = "none")

p3

# Style D: Combined Violin & Boxplot
p4 <- ggplot(data, aes(x = Group, y = Value, fill = Group)) +
  geom_violin(alpha = 0.3) +
  geom_boxplot(width = 0.1, color = "black", outlier.shape = NA) +
  labs(title = "4. Violin + Box", subtitle = "Density + Summary statistics") +
  theme_minimal() +
  theme(legend.position = "none")

p4
# Question 1: Combine all plots into one layout? (Unified plot for the 4 plots)
p1 + p2 + p3 + p4

# Question 2: Try gamma distribution instead of normal distribution in the sampled data and give the new results. 
data_gamma <- data.frame(
  Group = rep(c("Alpha", "Beta", "Gamma"), each = 100),
  Value = c(rgamma(100, shape = 3), rgamma(100, shape = 5), rgamma(100, shape = 7))
)


# Style A: Standard Boxplot
p1_gamma <- ggplot(data_gamma, aes(x = Group, y = Value, fill = Group)) +
  geom_boxplot() +
  labs(title = "1. Standard", subtitle = "Classic quartiles & outliers") +
  theme_minimal() +
  theme(legend.position = "none")

# Style B: Notched Boxplot
p2_gamma <- ggplot(data_gamma, aes(x = Group, y = Value, fill = Group)) +
  geom_boxplot(notch = TRUE) +
  labs(title = "2. Notched", subtitle = "Confidence intervals for medians") +
  theme_minimal() +
  theme(legend.position = "none")

# Style C: Boxplot with Jittered Points
p3_gamma <- ggplot(data_gamma, aes(x = Group, y = Value, fill = Group)) +
  geom_boxplot(outlier.shape = NA, alpha = 0.7) +
  geom_jitter(width = 0.2, alpha = 0.4, size = 1) +
  labs(title = "3. With Jitter", subtitle = "Shows raw data distribution") +
  theme_minimal() +
  theme(legend.position = "none")

# Style D: Combined Violin & Boxplot
p4_gamma <- ggplot(data_gamma, aes(x = Group, y = Value, fill = Group)) +
  geom_violin(alpha = 0.3) +
  geom_boxplot(width = 0.1, color = "black", outlier.shape = NA) +
  labs(title = "4. Violin + Box", subtitle = "Density + Summary statistics") +
  theme_minimal() +
  theme(legend.position = "none")

p1_gamma + p2_gamma + p3_gamma + p4_gamma
