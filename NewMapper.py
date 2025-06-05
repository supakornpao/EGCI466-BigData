#!/usr/bin/env python3
import csv
import sys
with open("/content/drive/MyDrive/Big Data Project(Spotify)/spotify-data.csv", mode ='r')as file:
  reader = csv.reader(file)
  with open("/content/drive/MyDrive/Big Data Project(Spotify)/demofile.txt", mode = 'w')as demofile:
    for index,row in enumerate(reader):
      if(index != 0):
        print(f"{row[2]}\t")
        demofile.write(f"{row[2]}\n")
