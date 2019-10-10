#Instructions
# 1. Total number votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#extensions to read/open file 
import csv
import os

# Assign a variable for the file to load and analysis.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #the first row of headers
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

print(total_votes)
print(candidate_options)





