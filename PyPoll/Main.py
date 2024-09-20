# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "election_analysis.txt")  # Output file path


with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    csv_data = [row for row in reader]

# print(csv_data)

# The total number of votes cast
total_votes = 0

for i in range(len(csv_data)):
    total_votes += 1

# print(total_votes)


# A complete list of candidates who received votes

candidates_list = []

for x in range(len(csv_data)):
    if csv_data[x][2] not in candidates_list:
        candidates_list.append(csv_data[x][2])

# print(candidates_list)

# The percentage of votes each candidate won



Charles_Casper_Stockham = 0
Diana_DeGette=0
Raymon_Anthony_Doane=0

for y in range(len(csv_data)):
    if csv_data[y][2] == 'Charles Casper Stockham':
        Charles_Casper_Stockham+=1
    if csv_data[y][2] == 'Diana DeGette':
        Diana_DeGette+=1
    if csv_data[y][2] == 'Raymon Anthony Doane':
        Raymon_Anthony_Doane+=1

Charles_Casper_Stockham = Charles_Casper_Stockham / len(csv_data) *100
Charles_Casper_Stockham = round(Charles_Casper_Stockham,3)
Diana_DeGette= Diana_DeGette / len(csv_data) *100
Diana_DeGette = round(Diana_DeGette,3)
Raymon_Anthony_Doane = Raymon_Anthony_Doane / len(csv_data) *100
Raymon_Anthony_Doane = round(Raymon_Anthony_Doane,3)



print(Charles_Casper_Stockham,
Diana_DeGette,
Raymon_Anthony_Doane)