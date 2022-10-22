def my_func(a,b,c=0,d=0,e=0,f=0,g=0):
    #returns 5% of the sum of a nad b
    return sum((a,b,c,d,e,f)) * 0.05


def my_func2(*args): # can be anything *spam 
    print(args)
    for item in args:
        print(item)
    return sum(args) *0.05

def my_func3(**kwargs): # can be anything **spam 
    print(kwargs)
    if 'name' in kwargs:
        print('The name {} in db '.format(kwargs['name']))
    else:
        print('The name {} not in db '.format(kwargs['name']))



def my_func4(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
    print('I would like {} {}s'.format(args[1],kwargs['fruit']))
    print('I would like {} {}s'.format(args[2],kwargs['animal']))







if __name__ =="__main__":


    result = my_func(40,60,90,80,80,80,98)
    print(result)




    result2 = my_func2(40,60,90,80,80,80,98,22)
    print(f'args  {result2}')

    my_func3(name= 'jack', age = 99)

    my_func4(12,24,36,fruit='orange',food='eggs',animal ='duck')


    