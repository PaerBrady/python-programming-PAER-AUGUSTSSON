# Data Processing and Visualization Program

## Description
This Python program processes and visualizes data from a CSV file containing unlabelled data points. The program reads in the data, renames columns, adds extra data, and assigns labels to the data points based on specific conditions. The program then plots the data on a scatter plot, differentiating between data points based on their assigned labels.

## Functionality
The program consists of the following key steps:

1. **Read CSV Data:** 
	- The program reads data from a CSV file named unlabelled\_data.csv using pandas and creates a DataFrame ud.
2. **Column Renaming:** 
	-The columns are renamed by replacing specific numeric values (-1.885907518189583 and -1.997407599218205) with x and y to represent coordinate values.

3. **List Creation and Data Modification:**
	- The values from the x and y columns are extracted as lists.
	- New values are appended to the x and y lists from the variable header\_ud.
	- These lists are then converted back into a DataFrame ud\_1.
4. **Labeling:**
	- A new label column (new\_label) is created based on the x column.
	- A loop iterates through each row of the DataFrame and assigns labels based on the y value:
	- If y \> 0, the label is set to 1.
	- If y \<= 0, the label is set to 0.
	- The new\_label column is then converted to integers.
5. **Visualization:**
	- The data is plotted using matplotlib.
	- Points with label 0 are plotted in green, while points with label 1 are plotted in orange.
	- A line is also plotted based on predefined x\_range and y\_range.
6. **Convert to new CSV-file:**
	- This new dataframe with new\_label column is saved in a labelled\_data csv file.

## Requirements
To run this program, the following libraries are required:
- `pandas`
- `matplotlib`

You can install these libraries using `pip`:

	\`\`\`bash
	pip install pandas matplotlib

## Executing Program
1. Place the unlabelled\_data.csv file in the same directory as this script.
2. Run the program using Python:
	-`python your\_script\_name.py`

The program will display a scatter plot-diagram with labeled data points separated by a straight line on the X-axis.

## Help
### - N/A
## Authors
### - Pär Augustsson
## Version History
### - 0.1 :
- Initial release. 
## License
### Open Source.
## Acknowledgements 
- My classmate Mustafa Yosufi for all his help showing and tutoring me in how to make this program.
- For the README-template:[https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc).
- For Chat GPT helping me show how to write a summary of my program in a README-style (prompt: ”Kan du skriva en förklaring för detta program som en README.md?”).


