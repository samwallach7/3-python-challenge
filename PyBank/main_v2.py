#Import modules
import os
import csv

#Establish csv path
csv_path = os.path.join('Resources', 'budget_data.csv')

#Establish lists and variables
date = []
profit_losses = []
num_change_rows = 0
total_rev = 0
rev_change = []
rev_change_month = []

#Open csv file and establish headers
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_headers = next(csvreader)
    print(f'"CSV HEADER: {csv_headers}')
    previous_revenue = 0
    #Run through each row in csv and: add values to lists, determine monthly revenue changes
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
            rev_change.append(revenue - previous_revenue)
            previous_revenue = revenue
    for row in csvreader:
        revenue = int(row[1])
        total_rev += revenue
        rev_change_month.append(row[0], revenue - previous_revenue)
        previous_revenue = revenue


#Derive additional variables from data
date_length = len(date)
profit_losses_int = [eval(i) for i in profit_losses]
total_profit = 0
for value in profit_losses_int:
    total_profit += value
average_change = round((sum(rev_change) / num_change_rows), 2)
greatest_increase = max(rev_change)
greatest_decrease = min(rev_change)



# Final output -----------------------------------
print(f'Financial Analysis')
print(f'-----------------------------------')
print(f'Total Months: {date_length}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: ${greatest_increase}')
print(f'Greatest Decrease in Profits: ${greatest_decrease}')

#Establish the lines of data that will be enetered into the new txt file
lines = ["Financial Analysis", 
         "---------------------------------", 
         (f'Total Months: {date_length}'), 
         (f'Total: ${total_profit}'), 
         (f'Average Change: ${average_change}'), 
         (f'Greatest Increase in Profits: ${greatest_increase}'), 
         (f'Greatest Decrease in Profits: ${greatest_decrease}')]
#Estbalish the location of the new txt file
output_file = os.path.join('analysis', "financial_analysis.txt")
with open(output_file, "w") as f:
    for line in lines:
        f.write(line)
        f.write('\n')