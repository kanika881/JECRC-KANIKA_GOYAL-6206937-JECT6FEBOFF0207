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