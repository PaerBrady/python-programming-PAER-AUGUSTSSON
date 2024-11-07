""" This script uses pandas library to read datapoints.txt in csv_format in two dimensions.
    Numpy and matplotlib are used for graphing and calculations.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Raphael says: The data in datapoints.txt is not suitable for reading directly with pandas.
# The first row in the file is _not_ in csv format. Thus everything gets messed up.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# The documentation says that you can use skiprows=1 to avoid this problem.
train_data = pd.read_csv("datapoints.txt")

# The below shouldn't be necessary. ItCompared to what you have done, it would be less work 
# without using pandas -- you have kind of shot yourself in the foot by using it!

# Clean data
train_data.columns = train_data.columns.str.replace(
    "(", "").str.replace(")", "")
train_data.columns = train_data.columns.str.strip().str.replace(" ",
                                                                "_").str.capitalize()

# Create and drop columns and assign labels to a new column.
train_data["0-Pichu_1-Pikachu"] = train_data["Label_0-pichu"]
train_data = train_data.drop(["Label_0-pichu", "1-pikachu"], axis=1)

# Split dataset into two new variables for further analysis.
pichu = train_data[train_data["0-Pichu_1-Pikachu"] == 0]
pikachu = train_data[train_data["0-Pichu_1-Pikachu"] == 1]

# Plot Pichu and Pikachu features
plt.scatter(x=pichu["Width_cm"], y=pichu["Height_cm"], color="yellow")
plt.scatter(x=pikachu["Width_cm"], y=pikachu["Height_cm"], color="orange")

test_list = []

with open("testpoints.txt", "r") as test_file:
    test_file = test_file.readlines()
    for line in test_file:
        test_list.append(line)

# Raphael says: The data in testpoints is not suitable to convert directly to a pandas dataframe. 
test_data = pd.DataFrame(test_list, columns=["test_d"])
# Drop index
test_data = test_data.drop(0, axis=0)

# Raphael says: The below is overly complicated.  Again, you have made things difficult by using pandas.

# Extract and seperate data from test data frame and store values in seperate columns and remove unecessary column.
test_data["Width_cm"] = test_data["test_d"].str.split(
    "(").str.get(1).str.split(",").str.get(0)
test_data["Height_cm"] = test_data["test_d"].str.split(
    ")").str.get(0).str.split(",").str.get(1)
test_data = test_data.drop("test_d", axis=1)
# Change objects in test_data to float.
test_data[["Width_cm", "Height_cm"]] = test_data[[
    "Width_cm", "Height_cm"]].astype(float)

# Create a function that takes data points from test_data-frame to compare to data points training data frame.

# Raphael Says: The below would be better written as a single function that takes the number of comparisons as a variable
def shortest_dist(width, height):
    dist_pikachu = []
    dist_pichu = []

    # Use euclidean distance formula to find shortets distance and add to list.
    for x, y in zip(pikachu["Width_cm"], pikachu["Height_cm"]):
        dist_pikachu.append(
            np.sqrt(np.power(x - width, 2) + np.power(y - height, 2)))

    for x, y in zip(pichu["Width_cm"], pichu["Height_cm"]):
        dist_pichu.append(
            np.sqrt(np.power(x - width, 2) + np.power(y - height, 2)))

    # Find the smallest distance in both lists and compare.
    shortest_pichu = min(dist_pichu)
    shortest_pikachu = min(dist_pikachu)

    if shortest_pichu < shortest_pikachu:
        return ("Pichu")
    else:
        return ("Pikachu")

# Show and print all 4 testpoints and closest label.
for x, y in zip(test_data["Width_cm"], test_data["Height_cm"]):
    de = shortest_dist(x, y)
    print(f"testpoint ({x}, {y}), classified as {de}")

# Compares width and hegit to the 10 nearest training data points.

# Raphael: Again, it would be better to write a single function that can compare to the N-nearest points.

def majority_dist(width1, height1):
    dist_dp = []
    # Calculate eucleadian distance and asign to list.
    for x, y in zip(train_data["Width_cm"], train_data["Height_cm"]):
        dist_dp.append(
            np.sqrt(np.power(x - width1, 2) + np.power(y - height1, 2)))
    sort_dp = sorted(dist_dp)
    minsta_df = sort_dp[:10]
    index_df = []
    for d in minsta_df:
        index_df.append(dist_dp.index(d))
    # Find 10 closest neighbors and return majority.
    pic_or_pika = train_data.loc[index_df, "0-Pichu_1-Pikachu"]

    if sum(pic_or_pika) > 5:
        return "Pikachu"
    else:
        return "Pichu"


# User interaction loop
while True:
    user_width = input("First: please enter a number for width: ")
    user_height = input("Second: Please enter a number for height: ")
    org_user_width = user_width
    org_user_height = user_height

    user_width = user_width.replace(".", "").replace("-", "")
    user_height = user_height.replace(".", "").replace("-", "")

    if user_width.isdigit() == False or user_height.isdigit() == False:
        print("is not a number")
    if user_width.isdigit() == True and user_height.isdigit() == True:
        if float(org_user_width) < 0 and float(org_user_height) < 0:
            print("is a negative number")
        elif float(org_user_width) > 0 and float(org_user_height) > 0:
            width_final = float(org_user_width)
            height_final = float(org_user_height)

            break

print(f"User input (width: {org_user_width}, height: {org_user_height}), classified as {
      shortest_dist(width_final, height_final)} by shortest distance")
print(f"User input (width: {org_user_width}, height: {org_user_height}), classified as {
    majority_dist(width_final, height_final)} by majority")
