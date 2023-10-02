import pandas as pd

#NOTE: do not code file path in script but as an argument!!
#try Jupyter notebook
#try github copilot

# Load the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

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

# Concatenate the sections horizontally to form the final DataFrame
intermediate_df = pd.concat(result_sections, axis=1)

# Divide each column of the intermediate DataFrame by its median value
result_df = intermediate_df.divide(intermediate_df.median())

# Print the resulting DataFrame with values divided by the last column of each section
print(result_df)