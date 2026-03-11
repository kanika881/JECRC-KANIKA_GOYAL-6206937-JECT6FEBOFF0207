import csv
from datetime import date
file=open("D:/capgemini/day10(10.03.2026)/csv_file_handling/expense.csv","a+")
w=csv.writer(file)

w.writerow(['DATE','CATEGORY','AMOUNT'])
w.writerows(
    [
        [date.today(),'Travel',2000],
        
        [date.today(),'Food','550'],
        
        [date.today(),'Movie',200],
        [date.today(),"concert",2000],
        
    ]
)

file.close()