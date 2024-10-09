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
