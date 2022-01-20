import os
import glob
import csv

GOOG = "GOOG"
MSFT = "MSFT"
IBM = "IBM"

def downloads(name):
    from urllib.request import urlopen
    url = "https://query1.finance.yahoo.com/v7/finance/download/{}?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true".format(name)

    local_path = os.path.join("C:\\Users\\klein\\Downloads\\{}.csv".format(name))
    with urlopen(url) as file, open(local_path, 'wb') as f:
        f.write(file.read())

downloads(GOOG)
downloads(IBM)
downloads(MSFT)

my_dir = 'C:\\Users\\klein\\Downloads'
csv_files = glob.glob(my_dir + "/**/*.csv", recursive = True)
print(csv_files)

def stock(name):
    with open("C:\\Users\\klein\\Documents\\{}_out.csv".format(name), "w", newline='') as name_out:
        with open("C:\\Users\\klein\\Downloads\\{}.csv".format(name), "r") as name:
            writer = csv.writer(name_out)
            for line in name:
                data = line.strip().split(",")
                if data[0] == "Date":
                    data.append("Change")
                else:
                    change = (float(data[4]) - float(data[1])) / float(data[1])
                    data.append(change)
                writer.writerow(data)
                print(data)

stock(GOOG)
stock(IBM)
stock(MSFT)
