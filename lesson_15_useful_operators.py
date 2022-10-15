mylist = [1,2,3]

for num in range(10):
    print(num)

print("==================")

for num in range(0,11,2):
    print(num)

print(list(range(0,11,2)))  #casting to list 

index_count =0
for letter in "abcde":
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count +=1

print("===================")

index_count = 0 
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count +=1 

print("===================")

index_count = 0 
word = 'abcde'
for item in enumerate(word) :
    print(item)
print("===================")
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
print("===================")


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c']
mylist3=[100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

print(list(zip(mylist1,mylist2,mylist3)))

for a,b,c in zip(mylist1,mylist2,mylist3):
    print(b)

print("===================")

print('x' in [1,2,3])
print('x' in ['x',2,3])
print("===================")

print('a' in 'a world')
print("===================")

print('mykey' in {'mykey':345})
d = {'mykey': 345}
print(345 in d.values())
print(345 in d.keys())
print("===================")

mylist = [10,20,30,100]
print(min(mylist))
print(max(mylist))
print("===================")

from random import shuffle

mlist= [1,2,3,4,5,6,7,8,9]

shuffle(mlist)
print(mlist)
shuffle(mlist)
print(mlist)

print("===================")

from random import randint
rrand=randint(0,100)
print(rrand)
print("===================")

result = input('What is your name ?')
print(result)

result = input('Fav number:')
print(result)
print(type(result))

result = int(input('fav num'))
print(result)
print(type(result))

result = float(input('fav num'))
print(result)
print(type(result))


