#Instructions
# 1. Total number votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. Create a list of counties

#extensions to read/open file 
import csv
import os

# Assign a variable for the file to load and analysis.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
counties_list = []
counties_votes = {}
largest_county = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #the first row of headers
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        county_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        if county_name not in counties_list:
            counties_list.append(county_name)
            counties_votes[county_name] = 0
        counties_votes[county_name] += 1

 
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------------\n"
        f"\nCounty Votes:\n"
        )
    print(election_results, end="")
    txt_file.write(election_results)
    for county in counties_list:
        votes_county = counties_votes[county]
        vote_percentage_county = (int(votes_county)/total_votes * 100)
        county_results = (
            f"{county}: {vote_percentage_county:.1f}% ({votes_county:,})\n"
            )
        print(county_results)
        txt_file.write(county_results)

        if votes_county > largest_county:
            largest_county = votes_county
            largest_turnout = county 
        turnout = (
            f"\n-----------------------------------\n"
            f"Largest County Turnout: {largest_turnout}\n"
            f"-----------------------------------\n"
            )
    print(turnout, end='')
    txt_file.write(turnout)

    for candidate in candidate_options:
        
        votes = candidate_votes[candidate]
        vote_percentage = (int(votes)/total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results) 
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------------\n") 
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

        




