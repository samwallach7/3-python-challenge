# Import modules
import os
import csv

# Establish csv path
csv_path = os.path.join('Resources', 'budget_data.csv')

# Establish lists and variables
date = []
profit_losses = []
num_change_rows = 0
total_rev = 0
rev_change_list = []
rev_change = 0

# Open csv file and establish headers (headers printed in terminal to confirm)
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_headers = next(csvreader)
    print(f'"CSV HEADER: {csv_headers}')
    previous_revenue = 0
    # Run through each row in csv and add values to lists
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(row[1])
        if previous_revenue == 0:
            revenue = int(row[1])
            total_rev += revenue
            previous_revenue = revenue
        elif previous_revenue != 0:
            revenue = int(row[1])
            num_change_rows += 1
            total_rev += revenue
            rev_change_list.append(revenue - previous_revenue)
            previous_revenue = revenue

# Derive additional variables from data, including max and min change variables to find their months
date_length = len(date)
average_change = round((sum(rev_change_list) / num_change_rows), 2)
greatest_increase = max(rev_change_list)
greatest_decrease = min(rev_change_list)

# Now that min and max profit change are defined, open the csv again and match the max and min values to a month
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_headers = next(csvreader)
    previous_revenue = 0
    for row in csvreader:
        if previous_revenue == 0:
            revenue = int(row[1])
            previous_revenue = revenue
        elif previous_revenue != 0:
            revenue = int(row[1])
            rev_change = revenue - previous_revenue
            if rev_change == int(greatest_increase):
                greatest_increase_month = str(row[0])
            elif rev_change == int(greatest_decrease):
                greatest_decrease_month = str(row[0])
            previous_revenue = revenue

# Final output for view on terminal
print(f'Financial Analysis')
print(f'-----------------------------------')
print(f'Total Months: {date_length}')
print(f'Total: ${total_rev}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

# Establish the lines of data that will be enetered into the new text file
lines = ["Financial Analysis", 
         "---------------------------------", 
         (f'Total Months: {date_length}'), 
         (f'Total: ${total_rev}'), 
         (f'Average Change: ${average_change}'), 
         (f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})'), 
         (f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')]
# Establish the location of the new text file
output_file = os.path.join('analysis', "financial_analysis.txt")
with open(output_file, "w") as f:
    for line in lines:
        f.write(line)
        f.write('\n')