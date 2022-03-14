#import requests
import os
import csv
import time

rootdir = "./iiitd"

for subdir, dirs, files in os.walk(rootdir):
     for file in files:
          filepath = subdir + os.sep + file
          if file.endswith("Power.csv"):
               csv_file = open(filepath)
               csvreader = csv.reader(csv_file)
               dir = subdir.split("\\")
               dir.pop(0)
               dir_join = ' '.join(dir)
               for row in csvreader:
                   t = float(row[0])
                   t = t/1000.0
                   t = int(t)
                   t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
                   #print("Local: " + dir_join +" Data: " + t + " Consumo em Kwh: " + row[1])
               csv_file.close()