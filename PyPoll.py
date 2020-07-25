# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Variable for the file to load and path
# file_to_load = 'Resources/election_results.csv'

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    
# To do: read and analyze the data here.    
    file_reader = csv.reader(election_data)
    
# Print each row in the CSV file.
    for row in file_reader:
        print(row)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


#To do: perform analysis.
    #print(election_data)

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

#Write some data to the file.
#    txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")
