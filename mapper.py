
import csv

with open('spotify-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['artists']}\t")
#artists: index 2
