# import os module to create file paths across operating systems
import os

# import module for reading csv files
import csv

# set path
csvpath = os.path.join('Resources', 'budget_data.csv')

# read csv
monthly_pl = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        monthly_pl.append(row)
        
# determine total months & net total profit/loss
months = []
profit_loss = []

for month in monthly_pl:
    months.append(month[0])
    profit_loss.append(int(month[1]))

total_months = len(months)
total_amount = sum(profit_loss)

# determine average revenue change, and greatest increase & decrease in profits
pl_flux = []

for i in range(1, len(profit_loss)):
    pl_flux.append(profit_loss[i] - profit_loss[i-1])

avg_flux = sum(pl_flux) / len(pl_flux)

greatest_increase_month = months[pl_flux.index(max(pl_flux)) + 1]
greatest_increase_profit = max(pl_flux)
greatest_decrease_month = months[pl_flux.index(min(pl_flux)) + 1]
greatest_decrease_profit = min(pl_flux)

# print to terminal
print("Financial Analysis")
print("-----------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${avg_flux: .2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})")

# write .txt file
txt_path = os.path.join('analysis', 'PyBank_results.txt')

with open(txt_path, 'w') as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("-----------------------------------------------------" + "\n")
    txtfile.write(f"Total Months: {total_months}" + "\n")
    txtfile.write(f"Total: ${total_amount}" + "\n")
    txtfile.write(f"Average Change: ${avg_flux: .2f}" + "\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})" + "\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})")
