x =25
def printer():
    x =50
    return x


print(x)
print(printer())
'''
LEGB Rule:
L : Local
E : Enclosing function locals 
G : Global
B : Build-in(Python)

'''
print("Example L : Local ")
result=lambda num : num**3
print(result)
print("==============")
print("Example E : Enclosing function locals  ")

name = " This is a global string "

def greet():
    name = 'Sammy'
    def hello():
        print('Hello ' + name)

    hello()
greet()
print("==============")


print("Example L E G ")
name = " I  am global variable  " #(Global)
def greet():
    #name = ' i am an Enclosing variable ' #(Enclosing)
    def hello():
    
        #name= 'I am a local variable '    #Local
        print('Hello ' + name)

    hello()
greet()

print("==============")

x = 50 
def func():
    global x
    print(f' X is {x} globally')

    # Local Reassignment on a global variable !
    x ='New Value '
    print(f"I just changed global  x to {x} ")


x = 50 
def func2(x):

    print(f' X is {x} globally')

    # Local Reassignment on a global variable !
    x ='New Value '
    print(f"I just changed global  x to {x} ")
    return x




if __name__ =="__main__":
 print(x)
 func()
 
 print(x)

 x =func2(x)
 print(x)








