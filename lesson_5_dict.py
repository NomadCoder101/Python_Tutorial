my_dict={'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':4.10}
print(prices_lookup['apple'])
print(prices_lookup['milk'])


d={'k1':123,'k2':[1,2,3,4],'k3':{'insideKey':100}}
print(d['k1'])
print(d['k2'])
print(d['k2'][3])
print(d['k3'])
print(d['k3']['insideKey'])

print("======================")

new_dict={'key1':['a','b','cat']}
print(new_dict)
my_list=new_dict['key1']
print(my_list)
letter=my_list[1]
print(letter)
letter=letter.upper()
print(letter)
print("======================")
print(new_dict['key1'][2].upper())
print(new_dict['key1'][2].title())

print("======================")
dk={'k1':100,'k2':200}
print(dk)
dk['k3']=300
print(dk)
dk['k1']='new value'
print(dk)
dk ={'k1':100,'k2':200,'k3':300}
print(dk)
print(dk.keys())
print(dk.values())
print(dk.items())
print("======================")



