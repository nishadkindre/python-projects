
#? Constructing a class used to create module info objects with it 

class Module:
    '''
    We construct a 'Module' class with methods defined under it to return the data about the module,classes under it,methods under the classes
    Using a combine object(preferably a zip object) containing all the data to be returned using the methods hereby defined
    '''

    l = ":"*30

    def __init__(self , name , data):
        '''
        Necessary to give the module name and the module data during object instantiation
        '''
        self.name = name
        self.Name = name.capitalize()
        self.data = data


    def getModuleInfo(self) :
        f'''
        Returns the information about the {self.Name} module.
        '''
        print(self.l)
        print(f"{self.Name} Module Info : ")
        print(self.l)
        exec(f"import {self.name}\
            \nprint({self.name}.__doc__)")


    def getClassesList(self):
        f'''
        Returns All The Classes defined under {self.Name} Module.
        '''
        print(self.l)
        print(f"{self.Name} Module Classes :")
        print(self.l)
        for i,j in enumerate(self.data,1) :
            print(i,j[0])


    def getClassInfo(self) :
        f'''
        Returns the information about the Specific Class of {self.Name} module ,
        using the input number given by the user.
        '''
        print(self.l)
        print("Enter Class Number : ")
        try : 
            cc = input()     
            c = int(cc)
            print(self.l)
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


    def getClassMethodsList(self) :
        f'''
        Returns All the Methods Under specific Class of {self.Name} Module.
        '''

        # refer : https://devnote.in/how-to-call-one-method-from-another-within-the-same-class-in-python/
        
        self.getClassesList()
        a = self.getClassInfo()
        try :         
            print(self.l)
            print("Methods under Class %s : " %(self.data[a-1][0]))
            for i,j in enumerate(self.data[a-1][2],1) : 
                print(i,j)
            print(self.l)
        except Exception as e:
            print("\033[1;31m")
            print(e)
        else :
            return a


    def getClassMethodInfo(self) :
            f'''
            Returns the information about the specific method of any {self.Name} class,
            using the input number given by the user.    
            '''        
            try :
                d = self.getClassMethodsList()
                print(self.l)
                print("\nEnter the Method Number : ")
                ee = input()
                e = int(ee)
                print(self.l)

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


    def getAll_ClassesMethods_ListsInfo(self) :  
        f'''
        Returns All Classes and Methods Under {self.Name} module it along with their information.
        '''

        for i in range(len(self.data)):
            print(self.l)
            print("Class ",self.data[i][0],":")
            print("Info :",self.data[i][1])
            print(self.l)
            print("Methods Under Class",self.data[i][0],":")

            for e in range(len(self.data[i][2])) :
                print("="*15,"\n*",e + 1,self.data[i][2][e],"method : \n")    # returns method name
                print(self.data[i][3][e])     # returns method info
            print(self.l)


    def run(self) :
        '''Run'''
        while True :
            print("\033[1;34m")
            print(self.l)
            print(f"Get {(self.Name)} Module Info")
            print(self.l)
            print("\033[1;36m")
            a = input(f' Enter 1 : {self.Name} Module Info          \
                      \n Enter 2 : Classes Under {self.Name} Module \
                      \n Enter 3 : Get Class Info                     \
                      \n Enter 4 : Get Class Methods List             \
                      \n Enter 5 : Get Class Method Info              \
                      \n Enter 6 : Get All Info                       \
                      \n Enter 7 : Exit \n ')
            print(self.l)

            if a == "1" :
                self.getModuleInfo()

            elif a == "2" :
                self.getClassesList()

            elif a == "3" :
                self.getClassInfo()

            elif a == "4" :
                self.getClassMethodsList()

            elif a == "5" :
                self.getClassMethodInfo()

            elif a == "6" :
                self.getAll_ClassesMethods_ListsInfo()

            elif a == "7" :
                print("\033[1;32m")
                print("Thank You!")
                print(self.l)
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
    We construct a 'Module_' class with methods defined under it to return the data about the module,and the methods under it
    Using a combine object(preferably a zip object) containing all the data to be returned using the methods hereby defined
    '''

    l = "\n" + ":"*30 + "\n"

    def __init__(self , name , data) :
        '''
        Necessary to give the module name and the module data during object instantiation
        '''
        self.name = name
        self.Name = name.capitalize()
        self.data = data


    def getModuleInfo(self) :
        f'''
        Returns the information about the {self.Name} module.
        '''
        print(self.l)
        print(f"{self.Name} Module Info : ")
        print(self.l)
        exec(f"import {self.name}\
            \nprint({self.name}.__doc__)")


    def getMethodList(self):
        f'''
        Returns All The Methods defined under {self.Name} Module In a Systematic manner
        '''
        print(self.l)
        print(f"{self.Name} Methods :")
        print(self.l)
        for i,j in enumerate(self.data,1) :
            print(i,j[0])
            

    def getMethodInfo(self , c) :
        f'''
        Returns the information about the {self.Name} module method ,
        using the input number given by the user as an argument while calling the function.
        '''
        self.c = c
        print(self.data[self.c-1][0] , "Method -->")
        print(self.data[self.c-1][1])
        print("-"*50)


    def returnMethodInfo(self) :
        '''
        To Return the specific info of a module method entered by user , thus calling getMethodInfo() function
        '''
        print(self.l)
        try :        
                c = int(input("Enter Method number : "))
                print(self.l)
                self.getMethodInfo(c)

        except ValueError :
            print("\033[1;31m")
            print("\t***Please Enter In Number Format Only***")

        except IndexError :
            print("\033[1;31m")
            print("\t***Please Enter Number within range***")


    def exportInfo(self) :
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
        b = "self.returnAllMethodsInfo()" 
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


    def returnAllMethodsInfo(self):
        methods_all = tuple(map(lambda a : self.getMethodInfo(a) , range(1,len(self.data) + 1)))
        print(methods_all[:-(len(self.data))])


    def run(self) :
        while True :
            print("\033[1;34m")
            print(self.l)
            print(f"Get {self.Name} Module Info")
            print(self.l)
            print("\033[1;36m")
            a = input(f" Enter 1 : {self.Name} Module info          \
                      \n Enter 2 : Method List                      \
                      \n Enter 3 : Method Info                      \
                      \n Enter 4 : Export All Info To a Text File   \
                      \n Enter 5 : Get All Methods Info             \
                      \n Enter 6 : Exit \n ")
            print(self.l)

            if a == "1" : 
                self.getModuleInfo()

            elif a == "2" : 
                self.getMethodList()

            elif a == "3" :
                self.returnMethodInfo()

            elif a == "4" :
                self.exportInfo()

            elif a == "5" : 
                self.returnAllMethodsInfo()

            elif a == "6" :
                print("\033[1;32m")
                print("Thank You!")
                print(self.l)
                break

            elif all(x.isdigit() for x in a) == False :
                print("\033[1;31m")
                print("\n***Please Enter In Number Format***\n")

            else :
                print("\033[1;31m")
                print("\n***Please Enter Number within range***\n")    
