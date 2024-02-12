import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from process_csv import get_season_summary

'''
1. Predict points per 90
2. scale by expected minutes. 

3. give a player name, their next fixture(s) and predict points
### does not include injuries 
 '''
# Assuming seasons_summary is your data
seasons_summary = get_season_summary()

# Determine the number of subplots needed
n_seasons = len(seasons_summary)
n_cols = 3  
n_rows = 3

# Create a figure and a set of subplots
fig, axs = plt.subplots(n_rows, n_cols, figsize=(12, n_rows * 4))
fig.tight_layout(pad=6.0)  # Add space between plots

# Flatten the array of Axes objects for easy iteration, if necessary
axs = axs.flatten()

# Loop through seasons and plot
for i, season in enumerate(seasons_summary):
    xp = []
    yp = []
    for row in seasons_summary[season].head(10).itertuples(index=True, name='Pandas'):
        xp.append(f"{row.first_name} {row.second_name}")
        yp.append(row.total_points)
    axs[i].bar(xp, yp)
    axs[i].set_title(f"Top Players for Season: {season}")
    axs[i].set_xlabel('Player')
    axs[i].set_ylabel('Season Point Total')
    axs[i].tick_params(labelrotation=90)  # Rotate labels for readability

# Adjust layout to make room for titles and labels
plt.tight_layout()

# Show the figure with all subplots
plt.show()

# # Set the title and labels for the axes
# plt.title('Net Transfer Spending vs Average Points per Season (18-23)')
# plt.xlabel('Net Transfer Spending Last 5 Seasons (€ in millions)')
# plt.ylabel('Average Points Per Season')