from modules import *

def run_module(num: str):
    number = int(num)
    module = (time, pandas, schedule, os, numpy, random, datetime, collection)
    try:
        return module[number-1].run()
    except Exception:
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

        input_ = input(' Enter 1 : Time Module         \
                      \n Enter 2 : Pandas Module       \
                      \n Enter 3 : Schedule Module     \
                      \n Enter 4 : OS Module           \
                      \n Enter 5 : Numpy Module        \
                      \n Enter 6 : Random Module       \
                      \n Enter 7 : Datetime Module     \
                      \n Enter 8 : Collections Module  \
                      \n Enter 0 : Exit \n' )

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
