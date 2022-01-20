import csv
import os

from urllib.request import urlopen
url = "https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true"

local_path = os.path.join("C:\\Users\\klein\\Downloads\\MSFT.csv")
with urlopen(url) as file, open(local_path, 'wb') as f:
    f.write(file.read())

with open("C:\\Users\\klein\\Documents\\MSFT_out.csv", "w", newline='') as MSFT_out:
    with open("C:\\Users\\klein\\Downloads\\MSFT.csv", "r") as MSFT:
        writer = csv.writer(MSFT_out)
        for line in MSFT:
            data = line.strip().split(",")
            if data[0] == "Date":
                data.append("Change")
            else:
                change = (float(data[4]) - float(data[1])) / float(data[1])
                data.append(change)
            writer.writerow(data)
            print(data)