#Importing packages
import os 
import csv 


#Reading csv file 
csvpath = os.path.join('Resources','election_data.csv')

candidates = []

#Reading csv and header

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    csv_header = next(csvreader)
    
    #Creating number of votes variable
    for row in csvreader:
       candidates.append(row[2])
         

    cc = candidates.count("Charles Casper Stockham")  

    dd = candidates.count("Diana DeGette")  

    ra = candidates.count("Raymon Anthony Doane")

    total = len(candidates)
    
    #Percent of votes
    perc_cc = round(cc/total * 100, 3)

    perc_dd = round(dd/total * 100, 3)

    perc_ra = round(ra/total * 100, 3)

    #Determing the winner
    if cc > dd and cc > ra:
        Winner = "Charles Casper Stockham"
    elif dd > cc and dd > ra:
        Winner =  "Diana DeGette"
    else:
        Winner = "Raymon Anthony Doane"      

# Printing results in Terminal 
print("Election Results")
print("-------------------------")

print("Total Votes: " + str(total))

print("-------------------------")

print(f"Charles Casper Stockham: {perc_cc}%  ({cc})")

print(f"Diana DeGette: {perc_dd}%  ({dd})")

print(f"Raymon Anthony Doane: {perc_ra}%  ({ra})")

print("-------------------------")

print("Winner: " + Winner)

print("-------------------------")

#Writing results in text file 
with open("analysis/election_results.txt", "w") as file:
    
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total}\n")
    file.write("----------------------------\n")
    file.write(f"Charles Casper Stockham: {perc_cc}%  ({cc})\n")
    file.write(f"Diana DeGette: {perc_dd}%  ({dd})\n")
    file.write(f"Raymon Anthony Doane: {perc_ra}%  ({ra})\n")
    file.write(f"-------------------------\n")
    file.write(f"Winner: {Winner}\n")
    file.write("-------------------------\n")