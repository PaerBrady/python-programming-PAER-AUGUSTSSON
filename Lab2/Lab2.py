            # Use pandas library to read datapoints.txt in csv_format in two dimensions.
            # Use numpy to do power of 2.
            # Use matplotlib module to use pyplot to create a graph over data points. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train_data = pd.read_csv("datapoints.txt")

            # Clean data frame from unnecessary symbols and white spaces.  
train_data.columns = train_data.columns.str.replace("(", "").str.replace(")", "")
train_data.columns = train_data.columns.str.strip().str.replace(" ", "_").str.capitalize()

            # Create and drop columns and asign lebels to a new column. 
train_data["0-Pichu_1-Pikachu"] = train_data["Label_0-pichu"]
train_data = train_data.drop(["Label_0-pichu","1-pikachu"], axis = 1)
            #print(train_data.head())

            # Split dataset into two new variables for further analysis.
pichu = train_data[train_data["0-Pichu_1-Pikachu"] == 0]
pikachu = train_data[train_data["0-Pichu_1-Pikachu"] == 1]
            #print(pikachu)

            # Plot Pichu and Pikachu features on x and y axis and asign color.
plt.scatter(x = pichu["Width_cm"], y = pichu["Height_cm"], color = "yellow")
plt.scatter(x = pikachu["Width_cm"], y = pikachu["Height_cm"], color = "orange")
            #print(plt.show())

            # Create empty list for further data collection.
test_list = []

            # Open and read file testpoints.txt and collect lines as elements in a list.
with open("testpoints.txt", "r") as test_file: 
    test_file = test_file.readlines()
    for line in test_file:
        test_list.append(line)

            # Converting data into data frame and remove unecessary row.  
test_data= pd.DataFrame(test_list, columns= ["test_d"])
test_data = test_data.drop(0, axis = 0) 

            # Extract and seperate data from test data frame and store values in seperate columns and remove unecessary column.
test_data["Width_cm"] = test_data["test_d"].str.split("(").str.get(1).str.split(",").str.get(0)
test_data["Height_cm"] = test_data["test_d"].str.split(")").str.get(0).str.split(",").str.get(1)
test_data = test_data.drop("test_d", axis= 1)
            # Change objects in test_data to float.
test_data[["Width_cm", "Height_cm"]] = test_data[["Width_cm", "Height_cm"]].astype(float)

            # Create a function that takes data points from test_data-frame to compare to data points training data frame. 
def shortest_dist(width, height):
    dist_pikachu = []
    dist_pichu = []

            # Use euclidean distance formula to find shortets distance and add to list.
    for x, y in zip(pikachu["Width_cm"], pikachu["Height_cm"]):
        dist_pikachu.append(np.sqrt(np.power(x - width, 2) + np.power(y - height, 2)))  

    for x, y in zip(pichu["Width_cm"], pichu["Height_cm"]):
        dist_pichu.append(np.sqrt(np.power(x - width, 2) + np.power(y - height, 2)))

            # Find the smallest distance in both lists and compare.
    shortest_pichu = min(dist_pichu)
    shortest_pikachu = min(dist_pikachu)

    if shortest_pichu < shortest_pikachu: 
        return ("Pichu")                            #(f"testpoint {width, height} calssified as Pichu") 
    else: 
        return ("Pikachu")                         #(f"testpoint {width, height} calssified as Pikachu")
                                                #print(shortest_dist(20.5,34)) #retunerar None?
            # Show and print all 4 testpoints and closest label.   
for x, y in zip(test_data["Width_cm"], test_data["Height_cm"]):
    de = shortest_dist(x, y)
    print(f"testpoint ({x}, {y}), classified as {de}")
          

            # Create a function that takes two numeric inputs and compare them to the 10 nearest training data points.
def majority_dist(width1, height1):
   dist_dp = []
            # Calculate eucleadian distance and asign to list. 
   for x, y in zip(train_data["Width_cm"], train_data["Height_cm"]):
      dist_dp.append(np.sqrt(np.power(x - width1, 2) + np.power(y - height1, 2)))
            # Sort distance and extract 10 smallest distanceand store them in a list.  
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
            #print(majority_dist(20.5,34))

            # Create a loop to handle, debug and feedback user input. Create variable to manipulate user input for feedback. 
while True: 
    user_width = input("First: please enter a number for width: ")
    user_height = input("Second: Please enter a number for height: ") 
    org_user_width = user_width
    org_user_height = user_height

    user_width = user_width.replace(".", "").replace("-", "")
    user_height = user_height.replace(".", "").replace("-", "")
            # Check if user input is a valid number.
    if user_width.isdigit() == False or user_height.isdigit() == False:
          print("is not a number")
            # Convert user input into float and check if it's a negative number or positive number.
    if user_width.isdigit() == True and user_height.isdigit() == True:
         if float(org_user_width) < 0 and float(org_user_height) < 0:
           print("is a negative number")
           # If user inout is valid covert to float. 
         elif float(org_user_width) > 0 and float(org_user_height) > 0:
          width_final = float(org_user_width)
          height_final = float(org_user_height)
          break
            # Call my two functions and insert user input and print results. 
print(f"User input (width: {org_user_width}, height: {org_user_height}), classified as {shortest_dist(width_final, height_final)} by shortest distance")
print(f"User input (width: {org_user_width}, height: {org_user_height}), classified as {majority_dist(width_final, height_final)} by majority")        
 










