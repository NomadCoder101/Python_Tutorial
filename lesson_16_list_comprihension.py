mystring = 'hello'
mylist =[]
for letter in mystring:
    mylist.append(letter)

print(mylist)
print("==============")

mylist= [letter for letter in mystring]
print(mylist)

mylist2=[x for x in 'word']
print(mylist2)

mylist3 = [num for num in range(0,11)]
print(mylist3)

mylist3 = [num**2 for num in range(0,11)]
print(mylist3)

mylist=[x for x in range(0,11) if x%2 ==0]
print(mylist)


mylist=[x**2 for x in range(0,11) if x%2 ==0]
print(mylist)
print("===================")

celcius = [0,10,20,34.5]
fahrenhiet = [((9/5)*temp + 32) for temp in celcius]
print(fahrenhiet)

fahrenhiet = []
for temp in celcius:
    fahrenhiet.append((9/5*temp +32))
print(fahrenhiet)  

print("===================")

result = [x if x%2 ==0 else 'ODD' for x in range(0,11)]
print(result)

print("===================")

mylist= []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)

print("===================")

mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
print(mylist)