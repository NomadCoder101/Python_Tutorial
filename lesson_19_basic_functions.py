
from unittest import result


def say_hello():
    print("hello")
    print('How')


say_hello()
print("==================")

def say_hello2(name):
    print(f'Hello {name}')

say_hello2('Jose')


print("==================")

def say_hello3(name ='Default'):
    print(f'Hello {name}')
    return (f'Hello {name}')

r = say_hello3()
print(r + '\t r ')


print("==================")

def add_num(num2,num1):
    return num1 + num2

result = add_num(10,20)
print(result)

print("==================")

def print_result(a,b):
    print(a+b) # cannot save to variable 

def return_result(a,b):#can save to variable 
    return a + b

print_result(10,20)
result = print_result(10,20)
print(result)
print("==================")
return_result(10,20)
result = return_result(10,20)
print(result)

print("==================")

def sum_num(a,b):
    return a+b

print(sum_num(10,20))

print(sum_num('10','20'))
