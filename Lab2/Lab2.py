# Use pandas library to read datapoints.txt in csv_format in two dimensions.
# Use numpy to do squre power in eucleadian distances.
# Use matplotlib module to use pyplot to create a graph over my data points. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dp = pd.read_csv("datapoints.txt")

# Clean dataframe from unnecessary symbols and white spaces.  
dp.columns = dp.columns.str.replace("(", "").str.replace(")", "")
dp.columns = dp.columns.str.strip().str.replace(" ", "_").str.capitalize()

#Create and drop columns and asign iy to a new column. 
dp["0-Pichu_1-Pikachu"] = dp["Label_0-pichu"]
dp = dp.drop(["Label_0-pichu","1-pikachu"], axis = 1)
    #print(dp.head())

#Split dataset in dp into two new variables for further analysis.
pichu = dp[dp["0-Pichu_1-Pikachu"] == 0]
pikachu = dp[dp["0-Pichu_1-Pikachu"] == 1]
    #print(pichu)

# Plot Pichu & Pikachu features on x and y - axis and asign color.
plt.scatter(x = pichu["Width_cm"], y = pichu["Height_cm"], color = "yellow")
plt.scatter(x = pikachu["Width_cm"], y = pikachu["Height_cm"], color = "orange")
    #print(plt.show())

# Create empty list for further data collection.
test_list = []

# Open and read file and collect and asign lines elements in a list.
with open("testpoints.txt", "r") as test_file: 
    test_file = test_file.readlines()
    for line in test_file:
        test_list.append(line)

# Converting data into data frame and clean data.  
test_data = pd.DataFrame(test_list, columns= ["test_d"])
test_data = test_data.drop(0, axis = 0) 

# Extracts data 3from data frame and stores values in separate colum. 
test_data["Width_cm"] = test_data["test_d"].str.split("(").str.get(1).str.split(",").str.get(0)
test_data["Height_cm"] = test_data["test_d"].str.split(")").str.get(0).str.split(",").str.get(1)
test_data = test_data.drop("test_d", axis= 1)
    #print(test_data)

# Create a function that takes two input from the test_data-frame to compare to pikachu and pichu data points. 
def label_test_data(width, height):
    dist_pikachu = []
    dist_pichu = []

# Use euclidean distance formula to find shortets distance and add to list.
    for x, y in zip(pikachu["Width_cm"], pikachu["Height_cm"]):
        dist_pikachu.append(np.sqrt(np.power(x - width, 2) + np.power(y - height, 2)))  

    for x, y in zip(pichu["Width_cm"], pichu["Height_cm"]):
        dist_pichu.append(np.sqrt(np.power(x - width, 2) + np.power(y - height, 2)))

# Find the smallest distance in both lists.
    shortest_pichu = min(dist_pichu)
    shortest_pikachu = min(dist_pikachu)

    if shortest_pichu < shortest_pikachu: 
        print(f"testpoint {width, height} calssified as Pichu")
    else: 
        print(f"testpoint {width, height} calssified as Pikachu")
    #print(label_test_data(25, 32))


def lik(xx, yy):
   dist_dp = []
   for x, y in zip(dp["Width_cm"], dp["Height_cm"]):
      dist_dp.append(np.sqrt(np.power(x - xx, 2) + np.power(y - yy, 2)))
   sort_dp = sorted(dist_dp)
   minsta_df = sort_dp[:10]
   index_df = []
   for d in minsta_df:
      index_df.append(dist_dp.index(d))

   pic_pika = dp.loc[index_df, "0-Pichu_1-Pikachu"]
   if sum(pic_pika) > 5:
      print("pikachu")
   else:
      print("pichu")

# måste loopa pga av och break vid rätt först loop för input tills rätt. Vilken looop passar #While loop  Inne i loopen skriv instruktioner. Den input ska kollas om det är sträng skicka felmeddelande med feeback, om numerical ett steg till om den är positiv eller negativ om båda är sanna (true) rätt value bsedan break. import numpy as np
import numpy as np 

while True: 
    user_width = input("First, please enter a number for width:")
    user_height = input("Second, please enter a number for height:") 
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
          xxx = float(org_user_width)
          yyy = float(org_user_height)
          break
#label_test_data(xxx, yyy)
#lik(xxx, yyy)        
    #print(f"{hej} based on closest point")
    #print(f"{hejhej} based on majority")










