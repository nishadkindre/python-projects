'''
To construct Individual module objects in order to display their data.
'''

#? Constructing a class used to create module info objects with it 

X = "\n" + ":"*30 + "\n"

class Module:
    '''
    Constructing a 'Module' class with methods defined under it to return the data about the module,classes under it,methods under the classes.
    Using a combine object(preferably a zip object) containing all the data to be returned using the methods hereby defined.
    '''

    def __init__(self , name : str , data : object):
        '''
        Necessary to give the module name and the module data during object instantiation.
        '''
        self.name = name
        self.Name = name.capitalize()
        self.data = data


    def module_info(self) :
        f'''
        Returns the information about the {self.Name} module.
        '''
        print(X)
        print(f"{self.Name} Module Info : ")
        print(X)
        exec(f"import {self.name}\
            \nprint({self.name}.__doc__)")


    def classes_list(self):
        f'''
        Returns All The Classes defined under {self.Name} Module.
        '''
        print(X)
        print(f"{self.Name} Module Classes :")
        print(X)
        for i,j in enumerate(self.data,1) :
            print(i,j[0])


    def class_info(self) :
        f'''
        Returns the information about the Specific Class of {self.Name} module ,
        using the input number given by the user.
        '''
        print(X)
        print("Enter Class Number : ")
        try : 
            number = input()     
            c = int(number)
            print(X)

            if c in range(1,len(self.data) + 1):
                print("Class",self.data[c-1][0] , "\n")
                print("Info : \n",self.data[c-1][1] , "\n")
                print("-"*50)
                return c

            elif c < 0 :
                print("\033[1;31m")
                print("***Please Enter Only Positive Numbers***")

            else :
                print("\033[1;31m")
                print("***Please Enter Number within range***")

        except ValueError:
            print("\033[1;31m")
            print("***Please Enter In Number Format Only***")

        else :
            return c

        # refer : https://stackoverflow.com/questions/20768856/calling-a-variable-from-one-function-to-another-function-in-python 
        # refer : file - return_function_variable.py


    def class_method_list(self) :
        f'''
        Returns All the Methods Under specific Class of {self.Name} Module.
        '''

        # refer : https://devnote.in/how-to-call-one-method-from-another-within-the-same-class-in-python/
        
        self.classes_list()
        a = self.class_info()
        try :         
            print(X)
            print("Methods under Class %s : " %(self.data[a-1][0]))
            for i,j in enumerate(self.data[a-1][2],1) : 
                print(i,j)
            print(X)

        except Exception as e:
            print("\033[1;31m")
            print(e)

        else :
            return a


    def class_method_info(self) :
            f'''
            Returns the information about the specific method of any {self.Name} class,
            using the input number given by the user.    
            '''        
            try :
                d = self.class_method_list()
                print(X)
                print("\nEnter the Method Number : ")
                ee = input()
                e = int(ee)
                print(X)

                try :
                    if len(self.data[d-1][3])+1 > e > 0 :
                        print("="*15,"\n*",self.data[d-1][2][e-1],"method : \n")    # returns method name
                        print(self.data[d-1][3][e-1])   # returns method info
                    else :
                        print("\033[1;31m")
                        print('***Please Enter A Positive Number within range***') 

                except  :
                    print("\033[1;31m")
                    print("***Enter Correct Class Number to Proceed***")

            except ValueError :
                print("\033[1;31m")
                print("\t***Please Enter In Number Format Only***")


    def all_info(self) :  
        f'''
        Returns All Classes and Methods Under {self.Name} module it along with their information.
        '''

        for i in range(len(self.data)):
            print(X)
            print("Class ",self.data[i][0],":")
            print("Info :",self.data[i][1])
            print(X)
            print("Methods Under Class",self.data[i][0],":")

            for e in range(len(self.data[i][2])) :
                print("="*15,"\n*",e + 1,self.data[i][2][e],"method : \n")    # returns method name
                print(self.data[i][3][e])     # returns method info
            print(X)


    def run(self) :
        '''Run'''
        while True :
            print("\033[1;34m")
            print(X)
            print(f"Get {(self.Name)} Module Info")
            print(X)
            print("\033[1;36m")
            a = input(f' Enter 1 : {self.Name} Module Info          \
                      \n Enter 2 : Classes Under {self.Name} Module \
                      \n Enter 3 : Get Class Info                     \
                      \n Enter 4 : Get Class Methods List             \
                      \n Enter 5 : Get Class Method Info              \
                      \n Enter 6 : Get All Info                       \
                      \n Enter 7 : Exit \n ')
            print(X)

            if a == "1" :
                self.module_info()

            elif a == "2" :
                self.classes_list()

            elif a == "3" :
                self.class_info()

            elif a == "4" :
                self.class_method_list()

            elif a == "5" :
                self.class_method_info()

            elif a == "6" :
                self.all_info()

            elif a == "7" :
                print("\033[1;32m")
                print("Thank You!")
                print(X)
                break

            elif all(x.isdigit() for x in a) == False :
                print("\033[1;31m")
                print("\n***Please Enter In Number Format***\n")

            else :
                print("\033[1;31m")
                print("\n***Please Enter Number within range***\n")    

#? for modules with only methods

class Module_ :
    '''
    Constructing a 'Module_' class with methods defined under it to return the data about the module,and the methods under it.
    Using a combine object(preferably a zip object) containing all the data to be returned using the methods hereby defined.
    '''

    def __init__(self , name : str , data : object) :
        '''
        Necessary to give the module name and the module data during object instantiation.
        '''
        self.name = name
        self.Name = name.capitalize()
        self.data = data


    def module_info(self) :
        f'''
        Returns the information about the {self.Name} module.
        '''
        print(X)
        print(f"{self.Name} Module Info : ")
        print(X)
        exec(f"import {self.name}\
            \nprint({self.name}.__doc__)")


    def methods_list(self):
        f'''
        Returns All The Methods defined under {self.Name} Module In a Systematic manner.
        '''
        print(X)
        print(f"{self.Name} Methods :")
        print(X)
        for i,j in enumerate(self.data,1) :
            print(i,j[0])
            

    def method_info_(self , number : int) :
        f'''
        Returns the information about the {self.Name} module method ,
        using the input number given by the user as an argument while calling the function.

        Seperate Method made for use in the method_info() & all_info() method.
        '''
        self.number = number
        print(self.data[self.number-1][0] , "Method -->")
        print(self.data[self.number-1][1])
        print("-"*50)


    def method_info(self) :
        '''
        To Return the specific info of a module method entered by user , thus calling method_info_() function
        '''
        print(X)
        try :        
                number = int(input("Enter Method number : "))
                print(X)
                self.method_info_(number)

        except ValueError :
            print("\033[1;31m")
            print("\t***Please Enter In Number Format Only***")

        except IndexError :
            print("\033[1;31m")
            print("\t***Please Enter Number within range***")


    def export_info(self) :
        f'''
        To create a file with filename entered by the user 
        A file containing info about the {self.Name} Module , {self.Name} Module Methods
        '''

        import io, sys

        old_stdout = sys.stdout 
        new_stdout = io.StringIO() 
        sys.stdout = new_stdout 
        a = f"""\
        \nimport {self.name}\
        \nprint({self.name}.__doc__)
        """ 
        exec(a)
        module_info = sys.stdout.getvalue().strip()
        sys.stdout = old_stdout 

        old_stdout = sys.stdout 
        new_stdout = io.StringIO() 
        sys.stdout = new_stdout 
        b = "self.all_info()" 
        exec(b)
        methods_info = sys.stdout.getvalue().strip()
        sys.stdout = old_stdout 

        # refer : https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement
        #! no other solution found yet...

        # exec(f"import {self.name}")
        # module_info = self.name.__doc__

        file = input("Enter name for the new text file to be created : ")
        methods_list = "\n".join([i[0] for i in self.data])
        i = "\n" , ":"*50 , "\n"

        with open(f"{file}.txt" , "w") as f :
            f.writelines(i)
            f.write(f"{self.Name} Module")
            f.writelines(i)
            f.write(module_info)
            f.writelines(i)
            f.write(f"{self.Name} Module Methods : \n\n")
            f.write(methods_list)
            f.writelines(i)
            f.write("Methods Info : \n\n")
            f.write(methods_info)
            f.writelines(i)

        print("Created File : %s.txt Successfully!"  %(file))


    def all_info(self):
        methods_all = tuple(map(lambda a : self.method_info_(a) , range(1,len(self.data) + 1)))
        print(methods_all[:-(len(self.data))])


    def run(self) :
        while True :
            print("\033[1;34m")
            print(X)
            print(f"Get {self.Name} Module Info")
            print(X)
            print("\033[1;36m")
            a = input(f" Enter 1 : {self.Name} Module info          \
                      \n Enter 2 : Method List                      \
                      \n Enter 3 : Method Info                      \
                      \n Enter 4 : Get All Methods Info             \
                      \n Enter 5 : Export All Info To a Text File   \
                      \n Enter 6 : Exit \n ")
            print(X)

            if a == "1" : 
                self.module_info()

            elif a == "2" : 
                self.methods_list()

            elif a == "3" :
                self.method_info()

            elif a == "4" : 
                self.all_info()

            elif a == "5" :
                self.export_info()

            elif a == "6" :
                print("\033[1;32m")
                print("Thank You!")
                print(X)
                break

            elif all(x.isdigit() for x in a) == False :
                print("\033[1;31m")
                print("\n***Please Enter In Number Format***\n")

            else :
                print("\033[1;31m")
                print("\n***Please Enter Number within range***\n")    
