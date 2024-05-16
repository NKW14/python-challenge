import os 
import csv 



csvpath = os.path.join('Resources','election_data.csv')

candidates = []
#profit = []
#monthly = []

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #print(csvreader)

    csv_header = next(csvreader)
    #print(csv_header)

    for row in csvreader:
       candidates.append(row[2])
        #profit.append(row[1])  

    cc = candidates.count("Charles Casper Stockham")  

    dd = candidates.count("Diana DeGette")  

    ra = candidates.count("Raymon Anthony Doane")

    total = len(candidates)

    perc_cc = round(cc/total * 100, 3)

    perc_dd = round(dd/total * 100, 3)

    perc_ra = round(ra/total * 100, 3)

    if cc > dd and cc > ra:
        Winner = "Charles Casper Stockham"
    elif dd > cc and dd > ra:
        Winner =  "Diana DeGette"
    else:
        Winner = "Raymon Anthony Doane"      

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

