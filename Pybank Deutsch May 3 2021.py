# Pybank financial variables that we are looking for

Total_number_of_months = 0
Total_net_income_over_entire_period = []
Average_monthly_change_in_net_income = []
Monthly_change = []
Greatest_monthly_profit_increase = ["", 0]
Greatest_monthly_profit_decrease = ["", 999999999999999]
total_net = 0
monthly_change=[]

#Import and read file
import csv
with open(r"C:\users\deuts\P hw\budget_data.csv") as file:
    reader = csv.reader(file)
    header = next(reader) #read the header row
    #Extract the header row 
    row0 = next(reader) 
    Total_number_of_months += 1
    total_net += int(row0[1])
    prev_net = int(row0[1])
    for row in reader:
        #print(row)
        Total_number_of_months +=1
        total_net += int(row[1])
        
        net_change = int(row[1])-prev_net
        prev_net = int(row[1])
        #print(net_change)
        Total_net_income_over_entire_period += [net_change]
        monthly_change += [row[0]]
        
        #Calculate the greatest increase 
        if net_change > Greatest_monthly_profit_increase[1]:
            Greatest_monthly_profit_increase[0] = row[0]
            Greatest_monthly_profit_increase[1] = net_change
        #Calculate the greatest decrease
        if net_change < Greatest_monthly_profit_decrease[1]:
            Greatest_monthly_profit_decrease[0] = row[0]
            Greatest_monthly_profit_decrease[1] = net_change
    #Time to calculate the average net change
average_net_change = sum(Total_net_income_over_entire_period)/len(Total_net_income_over_entire_period)
average_net_change="${:,.2f}".format(average_net_change)
total_net="${:,.2f}".format(total_net)

Greatest_monthly_profit_increase = "${:,.2f}".format(Greatest_monthly_profit_increase[1])
Greatest_monthly_profit_decrease = "${:,.2f}".format(Greatest_monthly_profit_decrease[1])
results = (
    f'Financial Analysis \n' 
    f'Total Months: {Total_number_of_months} \n'
    f'Net Profit: {total_net} \n'
    f'Average Monthly Change: {average_net_change} \n'
    f'Greatest Increase in Profits: {Greatest_monthly_profit_increase} \n'
    f'Greatest Loss In Profits: {Greatest_monthly_profit_decrease}')
print(results)

with open('output.txt', "w") as txt_file:
    txt_file.write(results)