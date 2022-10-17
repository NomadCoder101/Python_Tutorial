from random import shuffle 




def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():
    guess = ''
    while guess not in ['0','1','2','3']:
        guess = input('Pick a number: 0,1, or 2,3 \n')
    return int(guess)

def check_guess(mylist,guess):
    if my_list[guess] == '2':
        print('Correct')
        print(my_list)
    else:
        print('Wrong Guess')
        print(mylist)


if __name__ == '__main__' :
#inital list

    my_list = ['','0','','2']

    #Shuffle the list
    mixedup_list = shuffle_list(my_list)

    #User guess
    guess = player_guess()

    #check guess

    check_guess(mixedup_list,guess)



    



"""
    #example = [1,2,3,4,5,6,7]
    #shuffle(example)
    #result = example
    #print(result)


    def shuffle_list(my_list):
        shuffle(my_list)
        return my_list

    #result = shuffle_list(example)

    #print(result)

    #my_list = ['','0','']
    #result= shuffle_list(my_list)
    #print(result)
    #print("=====================")

    ###

    def shuffle_list(my_list):
        shuffle(my_list)
        return my_list

    def player_guess():
        guess = ''
        while guess not in ['0','1','2']:
            guess = input('Pick a number: 0,1, or 2 ')
        return int(guess)

    #my_idex = player_guess()
    #print(my_idex)
    print("++++++++++++++++++++")

###


"""


