######objective of this script:
#1. read in csv file (large table with numeric entries, roughly 50 columns and 500 rows) 
#2. Split the table into sections ("sets") of equal column amount
#3. Divide each column of a section by the last column of that section
#4. Divide each cell value of a specific column by the respective column median
#5. Plot all column medians in a barplot

#import necessary libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt


def read_csv_file(file_name):
    """ loads the CSV file into a Dataframe"""
    try:
        # Read the CSV file using pandas
        df = pd.read_csv(file_name, sep =";")
        print("CSV file loaded successfully:")
        print(df.head())
        return df # return the DataFrame
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the file name is provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <file_name.csv>")
    else:
        # Get the file name from the command line argument
        file_name = sys.argv[1]

        # Call the function to read the CSV file
        read_csv_file(file_name)

df = read_csv_file(file_name) #assign variable (df) to loaded CSV file

# Define the number of columns in each section
section_size = 17 
# Calculate the amount of sections
number_of_sections = int(df.shape[1]/section_size)

# Split the DataFrame into sections
sections = [df.iloc[:, i:i+section_size] for i in range(0, len(df.columns), section_size)]

# Create a list to store the resulting sections after division
result_sections = []

# Iterate through the sections and divide each column by the last column of that section
for section in range(number_of_sections):
    last_column_name = list(sections[section].keys())[-1]  # Get the name of the last column
    temp_df = sections[section] #create temporary df for specific section
    section_divided = temp_df.iloc[:,0:section_size-1].div(temp_df[last_column_name], axis=0)  # Divide each column of the section by the last column
    result_sections.append(section_divided) #add columns to previously created list

# Concatenate the sections horizontally to form the intermediate DataFrame
intermediate_df = pd.concat(result_sections, axis=1)

# Divide each column of the intermediate DataFrame by its median value creating the final result dataframe
result_df = intermediate_df.divide(intermediate_df.median())

# Calculate medians of each column for plotting
medians = result_df.median()

# Create a bar plot of medians
plt.figure(figsize=(8, 6))
medians.plot(kind='bar', color='skyblue')
plt.xlabel('Columns')
plt.ylabel('Medians')
plt.title('Medians of DataFrame Columns')
plt.xticks(rotation=90)
plt.show()
#NOTE: the median should be the same for each column

#save the result dataframe to a new csv file
result_df.to_csv('sample_data_SW_normalized.csv', index=False)  # Set index=False if you don't want to write row indices to the CSV file