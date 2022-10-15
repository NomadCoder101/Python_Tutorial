print(2 % 2 )
print(3 % 2 )
print(41 % 40 )

print(20 %2 ==0)
print(21 %2 ==0)

print("++++++++++++++++++")

def even_check(num1):
    result = num1 %2 ==0
    return result

print(even_check(10))
result = even_check(11)
print(result)


print("++++++++++++++++++")

def even_check2(num1):
    
    return num1 %2 ==0

print(even_check2(45))
print("=============")

# Retrun true if any numbre is even in the list 

def check_even_list(num_list):
    for number in num_list:
        if number %2 == 0 :
            return True 
        else:
            pass
    return False

li = check_even_list([1,35,3,4])
print(li)


print("=============")

# Retrun all even in the list 

def check_even_list2(num_list):
    even_numbers = [] # place holder variable 

    for number in num_list:
        if number %2 == 0 :
            even_numbers.append(number)
        else:
            pass
    return even_numbers

li = check_even_list([1,35,3,4,6,8])
print(li)
print(check_even_list2([1,2,3,4,5,6,7,8,9,10]))
print(check_even_list2([1,3,5]))

print("=================================")
