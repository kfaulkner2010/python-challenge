Overview

This repository contains two Python scripts for, PyBank and PyPoll, designed to analyze financial and election data respectively.


PyBank

The PyBank script analyzes financial records to calculate:

•	Total number of months included in the dataset

•	Net total amount of “Profit/Losses” over the entire period

•	Changes in “Profit/Losses” over the entire period and the average of those changes

•	Greatest increase in profits (date and amount) over the entire period

•	Greatest decrease in profits (date and amount) over the entire period

PyPoll


The PyPoll script analyzes election data to determine:

•	Total number of votes cast

•	Complete list of candidates who received votes

•	Percentage of votes each candidate won

•	Total number of votes each candidate won

•	Winner of the election based on popular vote


Files


•	PyBank/main.py: Script for financial data analysis.

•	PyPoll/main.py: Script for election data analysis.

•	Resources/budget_data.csv: Input file for PyBank.

•	Resources/election_data.csv: Input file for PyPoll.

•	analysis/budget_analysis.txt: Output file for PyBank results.

•	Analysis/election_analysis.txt: Output file for PyPoll results.

Dependencies


•	Python 3.x

•	csv module

•	os module
