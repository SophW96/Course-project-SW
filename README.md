# Course-project-SW

Note: The sample data (sample_data_SW.csv) is a csv file containing 51 columns and several hundreds of rows. The entries are numeric values.
Both the sample data and python script should be downloaded from the repository.
The script can be executed from the command line with the following line "python course_project.py sample_data_SW.csv" (keep in mind to add the file path if necessary).

This script should carry out the following steps:
1. Read the csv file.
2. Divide the dataframe into several sections of equal column amount (17 columns).
3. Divide each column of each section by the last column of that section.
4. Divide each column value by the median value of the respective column.
5. Create a barplot (opens in a new window) of the resulting column medians (should be the same value for each column upon successful division).
6. Create a new csv file with the updated column values (sample_data_SW_normalized.csv).
