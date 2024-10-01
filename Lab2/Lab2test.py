import pandas as pd
import matplotlib as plt

df = pd.read_csv("datapoints.txt")
df.columns = df.columns.str.replace("(", "").str.replace(")", "")
df.columns = df.columns.str.strip().str.replace(" ", "_").str.capitalize()
df["0-Pichu_1-Pikachu"] = df["Label_0-pichu"]
df = df.drop(["Label_0-pichu","1-pikachu"], axis = 1)

ett = df[df["0-Pichu_1-Pikachu"] == 1]
noll = df[df["0-Pichu_1-Pikachu"] == 0]


plt.scatter(x = ett["Width_cm"], y = ett["Height_cm"], color = "green")
plt.scatter(x = noll["Width_cm"], y = noll["Height_cm"], color = "red")

test_list = []


# Öppna testdatan och läs in som testfil.   
with open("testpoints.txt", "r") as test_file: # tilldela filobjeette till "test_file"
    fil = test_file.readlines()
    for line in fil:
        test_list.append(line)

#omvandla datan till en dataframe
test_data = pd.DataFrame(test_list, columns= ["test_d"])
test_data = test_data.drop(0, axis = 0) 

#gör om data till lämlplig struktur 
test_data["Width_cm"] = test_data["test_d"].str.split("(").str.get(1).str.split(",").str.get(0)
test_data["Height_cm"] = test_data["test_d"].str.split(")").str.get(0).str.split(",").str.get(1)
test_data = test_data.drop("test_d", axis= 1)


#from sklearn.model_selection import train_test_split

#x_test = test_data[["Width_cm", "Height_cm"]]
#x_train = df[["Width_cm", "Height_cm"]]

#y_train = df["0-Pichu_1-Pikachu"]

eucledian samma princip 

läs avståndet på 150 tetspunkter 
läs 75 avstånd / läs 75 svtånd 

använd av for -loopar för att räkna ut a ståndet at frma det mionsta värdet 

minsta värdet är picachu eller pichu 

lägg in allt i en lista för att hotta minsta värdet 


#from sklearn.linear_model import LogisticRegression

#log_reg = LogisticRegression()
#log_reg = fit(x_train, y_train)

#prediction = log_reg.predict(x_test)
#prediction_test = log_reg.predict(test_data)

# hitta en algortim (vad ska vi förutsäga)

#from sklearn.metrics import confusion_matrix
#con_prediction = confusion_matrix(y_test, prediction) #utvärdera träningsdatan med 


#While True:

#x_input = input("enter_")