from modules import *

def run_module(num: str):
    number = int(num)
    module = (time, pandas, schedule, os, numpy, random, math, datetime, collection)
    try :
        return module[number-1].run()
    except IndexError :
        print(RED)
        print('***Please Enter Number within range***')    

def run():
    while 1: 
        x = ':'*21
        print(BLUE)
        print(x)
        print('   Get Module Info   ')
        print(x)
        print(PINK)
        print(' 1 : Time Module         \
             \n 2 : Pandas Module       \
             \n 3 : Schedule Module     \
             \n 4 : OS Module           \
             \n 5 : Numpy Module        \
             \n 6 : Random Module       \
             \n 7 : Math Module         \
             \n 8 : Datetime Module     \
             \n 9 : Collections Module  \
             \n 0 : Exit \n' )

        input_ = input('Enter Number : ')

        if input_ == '0': 
            print(GREEN)
            print('Thank You!')
            break

        elif all(a.isdigit() for a in input_) is False:
            print(RED)
            print('***Please Enter In Number Format***')

        else: 
            run_module(input_)

run()
