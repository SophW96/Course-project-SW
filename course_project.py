
######objective of this script:
#1. read in csv file (large table with numeric entries, roughly 30 columns and 500 rows) #NOTE: do not code file path in script but as an argument!
#2. Split the table into sections ("sets") of equal column amount
#3. Divide each column of a section by the last column of that section
#4. Divide each cell value of a specific column by the respective column median
#5. Plot all column medians in a barplot

#import necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('your_file.csv') #still needs to be coded as argument

# Define the number of columns in each section
section_size = 6

# Split the DataFrame into sections
sections = [df.iloc[:, i:i+section_size] for i in range(0, len(df.columns), section_size)]

# Create a list to store the resulting sections after division
result_sections = []

# Iterate through the sections and divide each column by the last column of that section
for section in sections:
    last_column_name = section.columns[-1]  # Get the name of the last column
    section_divided = section.divide(section[last_column_name], axis=1)  # Divide the section by the last column
    result_sections.append(section_divided)

# Concatenate the sections horizontally to form the intermediate DataFrame
intermediate_df = pd.concat(result_sections, axis=1)

# Divide each column of the intermediate DataFrame by its median value
result_df = intermediate_df.divide(intermediate_df.median())

# Print the resulting DataFrame with values divided by the last column of each section
print(result_df)

#plot the resulting medians (still needs to be coded)