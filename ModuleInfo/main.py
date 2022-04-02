from modules import *

def run_module(num : str) :
    number = int(num)
    module = (time , pandas , schedule , os , numpy , random , datetime , collection)
    try :
        return module[number-1].run()
    except Exception :
        print("\033[1;31m")
        print("\n***Please Enter Number within range***\n")    

def run() :
    while 1 : 
        zz = ":"*21
        print("\033[1;34m")
        print(zz)
        print("   Get Module Info   ")
        print(zz)

        input_ = input("\033[1;35m \
                        \n Enter 1 : Time Module         \
                        \n Enter 2 : Pandas Module       \
                        \n Enter 3 : Schedule Module     \
                        \n Enter 4 : OS Module           \
                        \n Enter 5 : Numpy Module        \
                        \n Enter 6 : Random Module       \
                        \n Enter 7 : Datetime Module     \
                        \n Enter 8 : Collections Module  \
                        \n Enter 0 : Exit \n " )

        if input_ == "0" : 
            print("\033[1;32m")
            print(zz)
            print("Thank You!")
            print(zz)
            break

        elif all(a.isdigit() for a in input_) == False :
            print("\033[1;31m")
            print("\n***Please Enter In Number Format***\n")

        else : 
            print("\033[1;34m")
            run_module(input_)

run()
