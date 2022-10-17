stock_prices=[('APPL',200),('GOOG',400),('MSFT',100)]

for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(ticker)  

for ticker,price in stock_prices:
    print(price +(0.1 *price)) 

print("=================================")

work_hours =[('john',100),('jack',4000),('jill',800),('Cassey',5000)]

def employee_check(work_hours):
    
    current_max=0
    employee_of_month =''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month=employee
        else:
            pass

    return(employee_of_month,current_max)
    
result = employee_check(work_hours)
print(result)
print("======================")
name,hours = employee_check(work_hours)
print(name)
print(hours)
print("======================")

print(f"The eployee of the month is ",employee_check(work_hours))
print("=================================")


    

