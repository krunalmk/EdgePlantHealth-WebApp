import csv
import sys
# sys.path.append('C:\Users\kruna\Documents\Capstone Project')

filename = 'stats.csv'

def readCSV( filename):
    res = ""

    with open( filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            # res += row

    return res


def writeCSV( filename, dataArray):
    with open( filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dataArray)
        # writer.writerow(["SN", "Movie", "Protagonist"])
        # writer.writerow(["Lord of the Rings", "Frodo Baggins"])
        # writer.writerow(["Harry Potter", "Harry Potter"])
    

def appendCSV( filename, dataArray):
    with open( filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dataArray)
        # writer.writerow(["Lord of the Rings", "Frodo Baggins"])
        # writer.writerow(["Harry Potter", "Harry Potter"])
    

# appendCSV( filename)
# readCSV( filename)