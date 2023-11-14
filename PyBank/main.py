import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

date = []
profit_losses = []
num_change_rows = 0
total_rev = 0
rev_change = []
rev_change_month = []

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_headers = next(csvreader)
    print(f'"CSV HEADER: {csv_headers}')
    previous_revenue = 0
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

line_3 = date_length
line_4 = total_profit
line_5 = average_change
line_6 = greatest_increase
line_7 = greatest_decrease



lines = ["Financial Analysis", 
         "---------------------------------", 
         (f'Total Months: {date_length}'), 
         (f'Total: ${total_profit}'), 
         (f'Average Change: ${average_change}'), 
         (f'Greatest Increase in Profits: ${greatest_increase}'), 
         (f'Greatest Decrease in Profits: ${greatest_decrease}')]
output_file = os.path.join('analysis', "financial_analysis.txt")
with open(output_file, "w") as f:
    for line in lines:
        f.write(line)
        f.write('\n')