# Lab 3: Data Processing and Visualization Program

This Python program processes and visualizes data from a CSV file containing unlabelled data points. The program reads in the data, renames columns, adds extra data, and assigns labels to the data points based on specific conditions. The program then plots the data on a scatter plot, differentiating between data points based on their assigned labels.
## Description
### Functionality

## Requirements

To run this program, the following libraries are required:
- `pandas`
- `matplotlib`

You can install these libraries using `pip`:

\`\`\`bash
pip install pandas matplotlib
Functionality

### Functionality
The program consists of the following key steps:

1. **Read CSV Data:** 
    - The program reads data from a CSV file named unlabelled_data.csv using pandas and creates a DataFrame ud.
2. **Column Renaming:** 
	-The columns are renamed by replacing specific numeric values (-1.885907518189583 and -1.997407599218205) with x and y to represent coordinate values.
3. **List Creation and Data Modification:**
	- The values from the x and y columns are extracted as lists.
	- New values are appended to the x and y lists from the variable header_ud.
	- These lists are then converted back into a DataFrame ud_1.
4. **Labeling:**
	- A new label column (new_label) is created based on the x column.
	- A loop iterates through each row of the DataFrame and assigns labels based on the y value:
	- If y \> 0, the label is set to 1.
	- If y \<= 0, the label is set to 0.
	- The new_label column is then converted to integers.
5. **Visualization:**
    - The data is plotted using matplotlib.
    - Points with label 0 are plotted in green, while points with label 1 are plotted in orange.
    - A line is also plotted based on predefined x_range and y_range.