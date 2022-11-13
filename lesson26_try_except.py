'''
def add(n1, n2):
    
    print(n1+n2)

num1 = input('Enter number \n')
num2 = 20

#add(num1,num2)
#print('SOmthnig happened')

#-------------------------




try:
    result = 10 + '10'
    #result = 10 + 10
    #print(result)
except:
    print('cannot add integers with strings ')
else:
    print('Add went well')
    print(result)




try:
    f = open('testfile3','w')
    f.write('Write a test a file ')
except TypeError:
    print('There was a type error!')
except OSError:
    print('you got an OS/IO error')

finally:
    print('I always run ')

'''

def ask_for_int():
    while True:
        try: 
            result = int(input('Please proivde a number : \n'))
        except:
            print('Whoops! not a number ')
            continue
        else:
            print('That is a valid number ')
            break
        finally:
            print('End of try/Except/Finally')
            print(' i will always run at the end ')

ask_for_int()