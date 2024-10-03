# Use pandas library to read datapoints.txt in csv_format in two dimensions.
import pandas as pd
import numpy as np

dp = pd.read_csv("datapoints.txt")

# Clean dataframe from unnecessary symbols and white spaces  
dp.columns = dp.columns.str.replace("(", "").str.replace(")", "")
dp.columns = dp.columns.str.strip().str.replace(" ", "_").str.capitalize()

#Create and drop columns and asign iy to a new column 
dp["0-Pichu_1-Pikachu"] = dp["Label_0-pichu"]
dp = dp.drop(["Label_0-pichu","1-pikachu"], axis = 1)

# Display first five rows of dataframe 
# print(dp.head())


#Split dataset in dp into two new variables for further analysis 
pichu = dp[dp["0-Pichu_1-Pikachu"] == 0]
pikachu = dp[dp["0-Pichu_1-Pikachu"] == 1]
#print(pichu)


#Create empty list for further data collection.
test_list = []

# Open and read file and collect and asign data.
with open("testpoints.txt", "r") as test_file: 
    test_file = test_file.readlines()
    for line in test_file:
        test_list.append(line)

# Converting data into data frame and clean data  
test_data = pd.DataFrame(test_list, columns= ["test_d"])
test_data = test_data.drop(0, axis = 0) 

# Transforming data into proper format and store it. 
test_data["Width_cm"] = test_data["test_d"].str.split("(").str.get(1).str.split(",").str.get(0)
test_data["Height_cm"] = test_data["test_d"].str.split(")").str.get(0).str.split(",").str.get(1)
test_data = test_data.drop("test_d", axis= 1)
#print(test_data)

# Skapar en funktion som beräknar test_datan och som skall få 2 inmatningar bredd och höjd.
#import numpy as np

def label_test_data(width, height):
    dist_pikachu = []
    dist_pichu = []

    for x, y in zip(pikachu["Width_cm"], pikachu["Height_cm"]):
        dist_pikachu.append(np.sqrt(np.power(x - width, 2) + np.power(y - height, 2))) #Eucledian distance formula  leta efter avstång mellan alla puntre per rad och kolumn för inmatat värde 

    for x, y in zip(pichu["Width_cm"], pichu["Height_cm"]): #Tar bara rad oavsett om det står 2,5,7 istället för rad i numeriks ordning 
        dist_pichu.append(np.sqrt(np.power(x - width, 2) + np.power(y - height, 2)))

    shortest_pichu = min(dist_pichu)
    shortest_pikachu = min(dist_pikachu)

# om pichu är mindre än pikachu skriv pichu annars skriv pikachu 
    if shortest_pichu < shortest_pikachu: 
        print(f"testpoint {width, height} calssified as Pichu")
    else: 
        print(f"testpoint {width, height} calssified as Pikachu")
print(label_test_data(25, 32))


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

#lik(19, 34)


#Create algortim for user datapoint as input and handle non numerical values and negative values and feedback user....
while True: 
    user_width = input("Please enter a postive number for width:")
    user_height = input("Please enter a negative number as height:") 
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
             lik(float(org_user_width), float(org_user_height))
             break








