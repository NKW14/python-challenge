import os 
import csv 
import pandas as pd
from pathlib import Path

bank_path = Path("Resources/budget_data.csv")

bank_df = pd.read_csv(bank_path, encoding="utf-8")

bank_df["Profit/Losses"] = bank_df["Profit/Losses"].astype(float)

month_count = len(bank_df["Date"].unique())

Total_profit = bank_df["Profit/Losses"].sum()

bank_df["month_change"] = bank_df["Profit/Losses"].diff()

#print(bank_df)



average =round(bank_df["month_change"].mean(), 2)


#print(average)

Greatest_inc =round(bank_df["month_change"].max(),0)

#print(Greatest_inc)
Greatest_dec = round(bank_df["month_change"].min(),0)




Greatest_inc2 = bank_df.loc[(bank_df["month_change"] == Greatest_inc)]
Greatest_dec2 = bank_df.loc[(bank_df["month_change"] == Greatest_dec)]

del Greatest_inc2["Profit/Losses"]
del Greatest_dec2["Profit/Losses"]

#print(Greatest_inc2)

month1 = Greatest_inc2["Date"].tolist()
month2 = Greatest_dec2["Date"].tolist()
#print(month1)

#Greatest_inc3 = Greatest_inc2["Date"].tolist()


#print(Greatest_inc3)

#print(Greatest_dec2)

   

print("Financial Analysis")

print("----------------------------")

print(f"Total Months: {month_count} ")

print(f"Total: {Total_profit} ")

print(f"Average Change: {average}")

print(f"Greatest Increase in Profits: {month1[0]} (${Greatest_inc})")

print(f"Greatest Decrease in Profits: {month2[0]} (${Greatest_dec})") 



