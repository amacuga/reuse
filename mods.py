import datetime as dt
import csv
import math

#Create a filename from the current date and time.
filename = dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d-%H-%M-%S.csv")

#Open the file with that filename.
with open(filename, 'w', newline='') as f:
  #Enable CSV writing to the file.
  writer = csv.writer(f)
  #Write a header row.
  writer.writerow(['i', 'j', 'gcd'])
  #Write the GCD for all (i,j) pairs from 0 to 100.
  for i in range (100):
    for j in range (100):
        writer.writerow([i, j, math.gcd(i, j)])
