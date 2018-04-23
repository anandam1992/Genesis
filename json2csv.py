import csv
import json

infile=open("C:/Users/ARINDAM/Desktop/json.json","r")
outfile=open("C:/Users/ARINDAM/Desktop/a.csv","w")

writer=csv.writer(outfile)

for row in json.loads(infile.read()):
        writer.writerow(row.values())
