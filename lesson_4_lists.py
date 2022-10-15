my_list=[1,2,3]
my_list2=['string',100,32.3]
print(my_list)
print(my_list2)
print(len(my_list2))

print(my_list2[0])
print(my_list2[1:])

my_list=['one','two','three']
another_list=['four','five']
print(my_list+another_list)
new_list= my_list+another_list
print(new_list)
new_list[0]='ONE ALL CAPS'
print(new_list)
new_list.append('six')
new_list.append('seven')
print(new_list)
new_list.pop()
print(new_list)
popped_item=new_list.pop()
print(popped_item)
popped_item=new_list.pop(0)
print(popped_item)
print(new_list)

new_list=['a','c','e','b','x']
num_list=[4,1,8,3]

new_list.sort()
print(new_list)
sorted_list=new_list
print(sorted_list)

num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)




