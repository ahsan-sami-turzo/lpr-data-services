import pandas as pd
import matplotlib.pyplot as plt

# Define the file path (replace with your actual file path)
file_path = "your_data.xlsx"

# Read the excel sheet using pandas
data = pd.read_excel(file_path, sheet_name="Sheet1")

# Select the columns for the heatmap
heatmap_data = data[["max-step-size", "evaporation-rate", "ticks"]]

# Create the heatmap
plt.figure(figsize=(10, 6))
heatmap = plt.pcolor(heatmap_data, vmin=heatmap_data["ticks"].min(), vmax=heatmap_data["ticks"].max())

# Add colorbar
plt.colorbar(heatmap)

# Add labels for axes
plt.xlabel("Max Step Size")
plt.ylabel("Evaporation Rate")

# Add tick labels for rows and columns (optional)
plt.xticks([0.5 + i for i in range(len(heatmap_data["max-step-size"].unique()))], heatmap_data["max-step-size"].unique(), rotation=45)
plt.yticks([0.5 + i for i in range(len(heatmap_data["evaporation-rate"].unique()))], heatmap_data["evaporation-rate"].unique())

# Add title
plt.title("Heatmap of Ticks vs Max Step Size and Evaporation Rate")

# Display the heatmap
plt.show()