


def square_it(num):
    return num ** 2

def splicer(mystring):
    if len(mystring)%2 ==0:
        return 'Even'
    else:
        return mystring[0]

def check_even(num):
    return num % 2 == 0




if __name__ == "__main__":

    my_num = [ 1,2,3,4,5,6]
    names=['Sam','John','Eve','vennn']

    print(map(square_it,my_num))

    for item in map(square_it, my_num):

        print(item)

print("=======Map Example ===========")

ls = list(map(square_it,my_num))
print(ls)

print("=======Map Example ===========")

ss = list(map(splicer,names))  
print(ss)
    
print("=======example  Filter ===========")
result =filter(check_even, my_num)
print(result)
result =list(filter(check_even, my_num))
print(result)

print("=======example  Filter ===========")
for  n in filter(check_even,my_num):
    print(n)


print("=======example  lambda (anonymous functions)===========")



square=lambda num: num ** 2

print(square(5))

my_nums = [1,2,3,4,56,78]
result1 = (map(lambda num: num ** 2,my_nums))
print(result1)
result2 = list((map(lambda num: num ** 2,my_nums)))
print(result2)


check_even = lambda num: num % 2 == 0
print(check_even(2))
result1=(filter(lambda num: num % 2 == 0,my_nums))
print(result1)
result2=list((filter(lambda num: num % 2 == 0,my_nums)))
print(result2)


names=['Sam','John','Eve','vennn']
result2 = map(lambda x:x[0],names)
print(result2)
result3 = list(map(lambda x:x[0],names))
print(result3)
result3 = list(map(lambda x:x[::-1],names))
print(result3)

