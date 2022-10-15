mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

for num in mylist:
    print('hello')

for num in mylist:
    #check for even
    if num %2 ==0:
        print(f'Even Number:{num}')
    else:
        print(f'Odd Number:{num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum)  
print(list_sum)  



mystring = 'Hello World'

for letter in mystring:
    print(letter)

for _ in 'Hello Crazy':
    print('Cool!')


tup =(1,2,3)
for item in tup:
    print(item)

my_new_list = [(1,2),(3,4),(5,6),(7,8)]
for item in my_new_list:
    print(len(my_new_list))
    print(item)

for (a,b) in my_new_list:
    print(a)
    print(b)

for a,b in my_new_list:
    
    print(b)

my_new_list = [(1,2,3),(4,5,6),(7,8,9)]

print('++++++++')

for a,b,c in my_new_list:

    print(a)
    print(b)
    print(c)
    
d = {'k1':1 , 'k2':2 ,'k3':3}
for item in d.items():
    print(item)

for key,value in d.items():
    print(value)
    print(key)

for value in d.values():
    print(value)

for key in d.keys():
    print(key)
