#importing packages
import os 
import csv 
import pandas as pd
from pathlib import Path

#Reading CSV
bank_path = Path("Resources/budget_data.csv")

with open(bank_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    csv_header = next(csvreader)

bank_df = pd.read_csv(bank_path, encoding="utf-8")



#Calculating Total months, Total Profit, Monthly Change and average monthly change
bank_df["Profit/Losses"] = bank_df["Profit/Losses"].astype(float)

month_count = len(bank_df["Date"].unique())

Total_profit = bank_df["Profit/Losses"].sum()

bank_df["month_change"] = bank_df["Profit/Losses"].diff()

average =round(bank_df["month_change"].mean(), 2)


# Getting greatest increases and turning them into python variables
Greatest_inc =round(bank_df["month_change"].max(),0)

Greatest_dec = round(bank_df["month_change"].min(),0)

Greatest_inc2 = bank_df.loc[(bank_df["month_change"] == Greatest_inc)]
Greatest_dec2 = bank_df.loc[(bank_df["month_change"] == Greatest_dec)]

del Greatest_inc2["Profit/Losses"]
del Greatest_dec2["Profit/Losses"]



month1 = Greatest_inc2["Date"].tolist()
month2 = Greatest_dec2["Date"].tolist()

#printing outputs in terminal   

print("Financial Analysis")

print("----------------------------")

print(f"Total Months: {month_count} ")

print(f"Total: {Total_profit} ")

print(f"Average Change: {average}")

print(f"Greatest Increase in Profits: {month1[0]} (${Greatest_inc})")

print(f"Greatest Decrease in Profits: {month2[0]} (${Greatest_dec})") 


#writing outputs in text file
with open("analysis/Financial_Analysis.txt", "w") as file:
    
    file.write("Financial_Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {month_count} \n")
    file.write(f"Total: {Total_profit} \n")
    file.write(f"Average Change: {average}\n")
    file.write(f"Greatest Increase in Profits: {month1[0]} (${Greatest_inc})\n")
    file.write(f"Greatest Decrease in Profits: {month2[0]} (${Greatest_dec})\n") 
    

