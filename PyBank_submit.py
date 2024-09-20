# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = r"C:\Users\X572490\OneDrive - Nissan Motor Corporation\Desktop\Starter_Code (2)\Starter_Code\PyBank\Resources\budget_data.csv"  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path



# Open and read the csv
with open(file_to_load,'r') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    csv_data = [row for row in reader]

# The total number of months included in the dataset
total_months = len([row[0] for row in csv_data])
print(total_months)

# The net total amount of "Profit/Losses" over the entire period
total = 0
for row in csv_data:
    total += int(row[1])
print(total)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
num_list = []

for row in csv_data:
    num_list.append(int(row[1]))
# print(num_list)

num_list_diff = []
for i in range(1,len(num_list)):
    num_list_diff.append(num_list[i] - num_list[i-1])
# print(num_list_diff)

average_change = sum(num_list_diff) / len(num_list_diff)
average_change = round(average_change,2)
# print(average_change)

# The greatest increase in profits (date and amount) over the entire period
max_change_month = []
months = []

for i in range(1, len(csv_data)):
    current_month = csv_data[i][0]
    current_value = int(csv_data[i][1])
    previous_value = int(csv_data[i-1][1])
    change = current_value - previous_value
    num_list_diff.append(change)
    months.append(current_month)

# Find the maximum change and corresponding month
max_change = max(num_list_diff)
max_change_index = num_list_diff.index(max_change)
max_change_month = months[max_change_index]


# print(max_change_month)       
# print(max_change)

# The greatest decrease in profits (date and amount) over the entire period
min_months = []

for i in range(1, len(csv_data)):
    current_month = csv_data[i][0]
    current_value = int(csv_data[i][1])
    previous_value = int(csv_data[i-1][1])
    change = current_value - previous_value
    num_list_diff.append(change)
    min_months.append(current_month)

# Find the maximum change and corresponding month
min_change = min(num_list_diff)
min_change_index = num_list_diff.index(min_change)
min_change_month = months[min_change_index]
# print(min_change)


print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_change_month} ${max_change}')
print(f'Greatest Decrease in Profits: {min_change_month} ${min_change}')


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
