# Use for , split() and if to create a statement that
#will print out words that start with 's'

st = 'Sam Print only the words that start with s in the sentence'

#print(st.split())
for word in st.split():
    if word[0]== 's' or word[0] =='S':

        print(word)
print("==============================")

for word in st.split():
    if word[0].lower() == 's':

        print(word)


print("==============================")


# USe range() to print all the even numbers from 0 -10.

print(list(range(0,11,2)))
print("==============================")

for num in range(0,10,2):
    print(num)

# use list comprehension to create a list of all 
#numbers between 1 -50 that are divisible by 3 

print([x for x in range(1,51) if x%3 == 0 ])
print("===================================")
for x in range(1,51):
    if x%3 == 0:
        print(x)
print("===================================")

# go through the string below and if the length of a word 
# is even print 'Even'
st = 'Print every word in this sentence that has an even number of letter '

for word in st.split():
    if len(word) %2 == 0:
        print(word + ' is even' ,len(word), 'alphabets')

print("===================================")
print([word for word in st.split() if len(word) %2 == 0])

print("===================================")

#Write a program that prints the integers from 1 to 100
# But for multiples of three print'Fizz' istead of number
#and for multiples of 5 print 'Buzz'. for numbers which
# are multiples of both three and 5 print 'FizzBuzz'

for num in range(1,101):
    if num %3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)


print("===================================")

# USe list Comprehension to create a list of the first letters of every word in the string below .

st = 'Create a list of the first letters of every word in the string'

print([word[0] for word in st.split()])



