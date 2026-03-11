import csv
from datetime import date
file=open("D:/capgemini/day10(10.03.2026)/csv_file_handling/expense.csv","a+")
r=csv.reader(file)
file.seek(0)
print(list(r))
file.close()