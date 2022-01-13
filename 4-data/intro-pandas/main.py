import pandas as pd

# Reads csv squirrel data as a DataFrame
sd = pd.read_csv('squirrel.csv')

# Counts how many squirrels in each color
gray = len(sd[sd["Primary Fur Color"] == "Gray"])
red = len(sd[sd["Primary Fur Color"] == "Cinnamon"])
black = len(sd[sd["Primary Fur Color"] == "Black"])

# Creates a dictionary with fur color and count lists
colors = {
    "Fur Color": ["Gray", "Cinnamon", "Black "],
    "Count": [gray, red, black],
}

# Creates a DataFrame from colors dict
colors_df = pd.DataFrame(colors)

# Saves DataFrame as csv file
colors_df.to_csv('colors.csv')
