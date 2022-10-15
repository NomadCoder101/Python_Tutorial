myfile = open("test.txt")
print(myfile.read())
contents=myfile.read()
print(contents)
myfile.seek(0)
print(myfile.readlines())
myfile.seek(0)
myfile.close()
print("------------------")


with open('test.txt',mode='a') as f:
    f.write("\nFour on Fourth")
with open('test.txt',mode='r') as f:
    print(f.read())

with open('new_test1.txt', mode='w') as f:
    f.write(" I created this new file ")
with open('new_test1.txt', mode='r') as f:
    print("------------------")
    print(f.read())





  


 
