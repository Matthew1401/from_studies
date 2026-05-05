library(ggplot2)
library(dplyr)
library(aplpack)  # For Chernoff-Flury Faces
library(patchwork) # To combine plots elegantly
library(gganimate) # Animated Graphics
library(gifski) # Required for GIF rendering
library(plotly) #Interact visualization

# Generate sample data
set.seed(42)
n <- 100
df <- data.frame(
  ID = 1:n,
  Height = rnorm(n, mean = 170, sd = 10),
  Weight = rnorm(n, mean = 70, sd = 12),
  Score = rbeta(n, 2, 5) * 100,
  Category = factor(sample(c("Group A", "Group B"), n, replace = TRUE))
)
# 1.Histogram
ggplot(df, aes(x = Height, fill = Category)) +
  geom_histogram(
    bins = 15,
    color = "white",
    alpha = 0.8,
    show.legend = FALSE
  ) +
  # Separate the groups into two panels for a clear layout
  facet_wrap(~Category) +
  # Customizing the aesthetic
  scale_fill_manual(values = c("Group A" = "#2c3e50", "Group B" = "#e74c3c")) +
  theme_minimal(base_family = "serif") +
  labs(
    title = "Frequency Distribution of Height",
    subtitle = "Standard histogram representation (n=100)",
    x = "Height (cm)",
    y = "Count (Frequency)"
  ) +
  theme(
    strip.text = element_text(face = "bold", size = 12),
    panel.grid.minor = element_blank()
  )

# 2.Kernel Density Plot
ggplot(df, aes(x = Height, fill = Category, color = Category)) +
  # Main Density Curve: adjust alpha for transparency and size for line thickness
  geom_density(alpha = 0.3, linewidth = 1.2, adjust = 1) +
  # Add a Rug Plot to the bottom to visualize individual data points (sampling density)
  geom_rug(alpha = 0.5) +
  # Use a professional color palette
  scale_fill_manual(values = c("Group A" = "#00AFBB", "Group B" = "#E7B800")) +
  scale_color_manual(values = c("Group A" = "#00AFBB", "Group B" = "#E7B800")) +
  # Clean, publication-ready theme
  theme_minimal(base_size = 14) +
  labs(
    title = "Kernel Density Estimation",
    subtitle = "Comparing Height distributions with individual sample rugs",
    x = "Height (cm)",
    y = "Estimated Density",
    fill = "Cohort",
    color = "Cohort"
  ) +
  theme(legend.position = "top")


# 3.Histogram and Kernel Density
p1 <- ggplot(df, aes(x = Height, fill = Category)) +
  geom_histogram(aes(y = after_stat(density)),
                 bins = 20,
                 alpha = 0.4,
                 position = "identity") +
  geom_density(alpha = 0.2, linewidth = 1) +
  scale_fill_manual(values = c("#69b3a2", "#404080")) +
  theme_minimal() +
  labs(title = "Distribution of Height",
       subtitle = "Histogram with Kernel Density Overlay",
       x = "Height (cm)",
       y = "Density")

p1

# 4.Scatter plot
p2 <- ggplot(df, aes(x = Height, y = Weight, color = Score)) +
  geom_point(size = 3, alpha = 0.7) +
  geom_rug(alpha = 0.3) +
  geom_smooth(method = "lm", color = "black", linetype = "dashed", se = FALSE) +
  scale_color_viridis_c(option = "magma") +
  theme_light() +
  labs(title = "Height vs. Weight",
       subtitle = "Color mapped to Score with Marginal Rugs")

p2

# 4.1. Animate scatterplot by Category
anim_plot <- ggplot(df, aes(x = Height, y = Weight, color = Category)) +
  geom_point(size = 4, alpha = 0.8) +
  theme_minimal() +
  labs(title = "Data for: {closest_state}") +
  transition_states(Category, transition_length = 2, state_length = 1) +
  enter_fade() +
  exit_shrink()
# Render and save as GIF
animate(anim_plot, renderer = gifski_renderer())
anim_save("animated_scatter.gif")

# 4.2. 3D Scatterplot
plot_3d <- plot_ly(
  df,
  x = ~Height,
  y = ~Weight,
  z = ~Score,
  color = ~Category,
  colors = c("blue", "orange"),
  type = "scatter3d",
  mode = "markers",
  marker = list(size = 5, opacity = 0.8, symbol = "circle")
) %>%
  layout(
    title = "3D Relationship: Height, Weight, and Score",
    scene = list(
      xaxis = list(title = "Height (cm)"),
      yaxis = list(title = "Weight (kg)"),
      zaxis = list(title = "Score (%)")
    ),
    margin = list(l = 0, r = 0, b = 0, t = 50)
  )

plot_3d

# 5.Chernoff-Flury Faces
# Standardize data for facial features
face_data <- df[1:9, c("Height", "Weight", "Score")]
# features are mapped to 15 different facial parameters
faces(face_data,
      main = "Chernoff-Flury Faces (First 9 Observations)",
      face.type = 1)
# Facial Feature 	  Mapped Variable (Example)
# Face   Height	    Height
# Smile  Curve	    Score
# Eye    Width	    Weight


# Question 1: The "Visual Illusion" of Density Scaling
# Context: In the Histogram and Kernel Density code, we used aes(y = after_stat(density)) to overlay a smooth curve on top of the bars.
# Task : Remove y = after_stat(density) from the geom_histogram() call and Modify the binwidth of your histogram to an extremely small value and then an extremely large value (e.g., 20).
# How does this "binning" choice change your perception of the data's normality compared to the "fixed" shape of the Kernel Density estimate?

p1_0 <- ggplot(df, aes(x = Height, fill = Category)) +
  geom_histogram(bins = 20, alpha = 0.4, position = "identity", binwidth = 0.01) +
  geom_density(alpha = 0.2, linewidth = 1) +
  scale_fill_manual(values = c("#69b3a2", "#404080")) +
  theme_minimal() +
  labs(title = "Distribution of Height", subtitle = "Histogram with Kernel Density Overlay", x = "Height (cm)", y = "Density")

p1_0

p1_1 <- ggplot(df, aes(x = Height, fill = Category)) +
  geom_histogram(bins = 20, alpha = 0.4, position = "identity", binwidth = 20) +
  geom_density(alpha = 0.2, linewidth = 1) +
  scale_fill_manual(values = c("#69b3a2", "#404080")) +
  theme_minimal() +
  labs(title = "Distribution of Height", subtitle = "Histogram with Kernel Density Overlay", x = "Height (cm)", y = "Density")

p1_1

# We do not know how to define the binwidth, and because of that the shape of the graph does not look normal, due to that.

#Question 2: Multidimensional Perception and Feature Mapping
#Context: Chernoff-Flury faces map different variables to specific facial features (e.g., smile, eye width, face height) to leverage human facial recognition for multivariate analysis.
#Task A: Normalize your df dataset using the scale() function before generating the faces. 
#Task B: Humans perceive certain facial features like the mouth curve (smile) or eye size more intensely than others, such as ear size. Re-map the faces() function to the 6th parameter (Smile Curve) so that this variable controls the smile or eye size. 

face_data <- df[1:9, c("Height", "Weight", "Score")]
faces(face_data,
      main = "Chernoff-Flury Faces (First 9 Observations)",
      face.type = 1)
