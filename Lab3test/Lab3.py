
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt


# Read CSV file into a DataFrame, display the columns of the DataFrame and create a list with two values.
ud = pd.read_csv("unlabelled_data.csv")
ud.columns
header_ud = [-1.885907518189583, -1.997407599218205]

# Rename the columns in the DataFrame, replacing specific strings with 'x' and 'y'
ud.columns = ud.columns.str.replace("-1.885907518189583", "x"). str.replace("-1.997407599218205", "y")

# Convert the 'x' and 'y' columns of the DataFrame to lists
x = list(ud["x"])
y = list(ud["y"])

# Append the values from header_ud to the respective lists
x.append(header_ud[0])
y.append(header_ud[1])

# Convert the lists back to DataFrames
ud_1 = pd.DataFrame(x, columns = ["x"])
ud_2 =  pd.DataFrame(y, columns = ["y"])
ud_1["y"] = ud_2



# Set range for x and y - axis
x_range = [-6, 6]
y_range = [0, 0]



ud_1["new_label"] = ud_1["x"]       # Assign the values of the "x" column to the new "label" column
         
for x in range(len(ud_1)):      # Loop through each row of the DataFrame
    if ud_1.loc[x, "y"] > 0:        # If the value in the "y" column of the current row is greater than 0
        ud_1["new_label"] = ud_1["new_label"].replace(ud_1.loc[x, "new_label"], 1)      # Replace the value in the "label" column with 1 for this condition
    else:
        ud_1["new_label"] = ud_1["new_label"].replace(ud_1.loc[x, "new_label"], 0)      # Replace the value in the "label" column with 0 if the condition is not met
ud_1["new_label"] = ud_1["new_label"].astype(int)       # Convert the "label" column to integers

label0 = ud_1[ud_1["new_label"] == 0]       # Create two DataFrames: one where the label is 0 and one where the label is 1
label1 = ud_1[ud_1["new_label"] == 1]

plt.scatter(x = label0["x"], y = label0 ["y"], color = "green")         # Plot the data where the label is 0 (green) and the label is 1 (orange)
plt.scatter(x = label1["x"], y = label1 ["y"], color = "orange")
plt.plot(x_range, y_range)      # Plot a line based on x_range and y_range (these should be defined elsewhere in the code)
plt.show



#ud_1.to_csv("labelled_data.csv", index=False)       # Save the updated DataFrame to a new CSV file without the index column
