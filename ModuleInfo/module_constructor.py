'''To construct Individual module objects in order to display their data.'''

X = ':'*30
RED = '\033[1;31m'
BLUE = '\033[1;34m'
PINK = '\033[1;35m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'

#? Constructing a class used to create module info objects with it. 
class ModuleC:
    '''Constructing a 'ModuleC' class 
    
    With methods defined under it to return the data about the 
    module, classes under it, methods under the classes, all info, export info
    
    Using a combine object(preferably a zip object converted to a tuple)
    containing all the data to be returned using the methods hereby defined.
    '''

    def __init__(self, name: str, data:  tuple) -> None:
        '''Necessary to define the module name and module data during object instantiation.
        
        param name: str, name of the module
        param data: tuple, a tuple object(containing the data) of the module to be created 
        '''
        self.name = name
        self.Name = name.capitalize()
        self.data = data

    def module_info(self) -> None:
        '''Returns the information about the Module.'''
        print(f'{self.Name} Module Info :')
        print('\n')
        exec(f'import {self.name}\
            \nprint({self.name}.__doc__)')

    def classes_list(self) -> None:
        '''Returns All The Classes defined under the Module.'''
        print(f'{self.Name} Module Classes :')
        print('\n')
        for i, j in enumerate(self.data, 1):
            print(i, j[0])

    def class_info(self) -> int:  # function returns an int value
        '''Returns the information about the Specific Class of the Module.
        
        Using the input number given by the user.
        '''
        print('Enter Class Number :')
        try: 
            number = input()     
            a = int(number)
            print(X)
            class_name: str = self.data[a-1][0]
            class_info: str = self.data[a-1][1]

            if a<=0:
                print(RED)
                print('***Please Enter Only Positive Numbers***')
            else: 
                print('Class', class_name, '\n')
                print('Info :\n', class_info, '\n')
                return a
                # refer : https://stackoverflow.com/questions/20768856/calling-a-variable-from-one-function-to-another-function-in-python 

        except ValueError:
            print(RED)
            print('***Please Enter In Number Format Only***')

        except IndexError:
            print(RED)
            print('***Please Enter Number within range***')

    def class_methods_list(self) -> int:
        '''Returns All the Methods Under Specific Class of the Module.'''
        
        # refer : https://devnote.in/how-to-call-one-method-from-another-within-the-same-class-in-python/
        self.classes_list()
        b: int = self.class_info()
        class_name: str = self.data[b-1][0]
        class_methods: tuple = self.data[b-1][2]
        try:         
            print(X)
            print(f'Methods under Class {class_name} :')
            for y, z in enumerate(class_methods, 1): 
                print(y, z)

        except Exception:
            print('.')  # prints when an exception occurs in the method called

        else:
            return b

    def class_method_info(self) -> None:
        '''Returns the information about the specific method of any class under the Module.
        
        Using the input number given by the user.    
        '''        
        try:
            c: int = self.class_methods_list()
            print(X)
            print('\nEnter the Method Number :')
            number = input()
            d = int(number)
            print(X)
            method_name: str = self.data[c-1][2][d-1]
            method_info: str = methods_info_list[d-1]
            methods_info_list: tuple = self.data[c-1][3]

            if d not in range(1, len(methods_info_list)+1):
                print(RED)
                print('***Please Enter A Positive Number within range***') 
            else:
                print(method_name, 'method :\n')
                print(method_info) 
            
        except ValueError:
            print(RED)
            print('***Please Enter In Number Format Only***')

        except Exception :
            print('***Enter Correct Class Number to proceed!***')  # prints when exception/s occurs in the methods called

    def all_info(self) -> None:  
        '''Returns All Classes and Methods Under the Module along with their information.'''
        x = '-'*30
        self.module_info()

        for i in range(len(self.data)):
            class_name: str = self.data[i][0]
            class_info: str = self.data[i][1]
            class_methods: tuple = self.data[i][2]
            print(X)
            print('Class ', class_name, '\n')
            print('Info :\n', class_info)
            print('\n')
            print(f'Methods Under Class {class_name} :\n')

            for j in range(len(class_methods)):
                method_name: str = self.data[i][2][j] + '()'
                method_info: str = self.data[i][3][j]
                print(x)
                print(j+1, '.', method_name, 'method :\n')
                print(method_info, '\n')
            print(X)

    def print_output(self, input_: str = 'self.all_info()') -> str:  # returns a str value , default parameter = 'self.all_info()'
        '''Helper Method.

        Return the output of an input(a function in our case) taken as an argument.
        For special purpose of printing output in a text file.

        Special Method for use in export_info() method.
        '''
        import io
        import sys
        old = sys.stdout 
        new = io.StringIO() 
        sys.stdout = new   
        exec(input_)
        output_ = sys.stdout.getvalue().strip()
        sys.stdout = old     

        return output_ 
        # refer : https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement

    def export_info(self) -> None:
        '''To create a file with filename entered by the user.
        
        A file containing info about the Module and it's Methods.
        '''       
        all_info = self.print_output()
        file = input('Enter New File name :')
        with open(f'{file}.txt', 'w') as f :
            f.write(all_info)
        print(f'Created File : {file}.txt Successfully!')

    def intro(self) -> None:
        print(BLUE)
        print(X)
        print(f'Get {self.Name} Module Info')
        print(X)
        print(CYAN)

    def run(self) -> None:
        '''Run'''
        while True :
            self.intro()
            print(f' 1 : {self.Name} Module Info           \
                  \n 2 : Classes Under {self.Name} Module  \
                  \n 3 : Class Info                        \
                  \n 4 : Class Methods List                \
                  \n 5 : Class Method Info                 \
                  \n 6 : All Info                          \
                  \n 7 : Export All Info To a Text File    \
                  \n 8 : Exit \n')

            input_ = input('Enter Number : ')  
            print(X)

            if all(x.isdigit() for x in input_) is False:
                print(RED)
                print('***Please Enter In Number Format***')

            elif input_ == '1':
                self.module_info()

            elif input_ == '2':
                self.classes_list()

            elif input_ == '3':
                self.class_info()

            elif input_ == '4':
                self.class_methods_list()

            elif input_ == '5':
                self.class_method_info()

            elif input_ == '6':
                self.all_info()

            elif input_ == '7':
                self.export_info()

            elif input_ == '8':
                print(GREEN)
                print('Thank You!')
                break

            else:
                print(RED)
                print('***Please Enter Number within range***')    

#? A Class For modules with only methods.
class Module(ModuleC):
    '''Constructing a 'Module' class. 
    
    With methods defined under it to return the data about the module,and the methods under it.
    Using a combine object(preferably a zip object converted to a tuple) 
    containing all the data to be returned using the methods hereby defined.
    
    Inherited Methods from ModuleC:
    module_info()
    export_info()
    intro()
    '''
    def methods_list(self) -> None:
        '''Returns All The Methods defined under the Module In a Systematic manner.'''
        print(f'{self.Name} Methods :\n')
        for y, z in enumerate(self.data, 1):
            print(y, z[0])
            
    def method_info_(self, number: int) -> None:
        '''Helper Method.

        Returns the information about the specific Module method.
        Using the input number given by the user as an argument while calling the function.

        Special Method for use in method_info() & all_info() method.
        '''
        x: str = '\n' + '-'*50
        self.number = number
        method_name: str = self.data[self.number-1][0] + '()'
        method_info: str = self.data[self.number-1][1]

        print(method_name, 'Method :')
        print(method_info)
        print(x)

    def method_info(self) -> None:
        '''Return the specific info of a Module method entered by user, 
        
        thus calling method_info_() function.
        '''
        try:        
            number = int(input('Enter Method number : '))
            print(X)
            self.method_info_(number)

        except ValueError:
            print(RED)
            print('***Please Enter In Number Format Only***')

        except IndexError:
            print(RED)
            print('***Please Enter Number within range***')

    def all_info(self) -> None:
        '''Returns All Methods Under the Module along with their information.'''
        all_methods_info = tuple(map(lambda a: self.method_info_(a), range(1, len(self.data)+1)))
        
        print(X)
        self.module_info()
        print(X)
        self.methods_list()
        print(X)
        print(all_methods_info[:-len(self.data)])

    def run(self) -> None:
        '''Run'''
        while True:
            self.intro()
            print(f' 1 : {self.Name} Module info          \
                  \n 2 : Method List                      \
                  \n 3 : Methods Info                     \
                  \n 4 : All Info                         \
                  \n 5 : Export All Info To a Text File   \
                  \n 6 : Exit \n')

            input_ = input('Enter Number : ')
            print(X)

            if all(i.isdigit() for i in input_) is False:
                print(RED)
                print('***Please Enter In Number Format***')

            elif input_ == '1': 
                self.module_info()
                
            elif input_ == '2': 
                self.methods_list()
                
            elif input_ == '3':
                self.method_info()

            elif input_ == '4': 
                self.all_info()

            elif input_ == '5':
                self.export_info()

            elif input_ == '6':
                print(GREEN)
                print('Thank You!')
                break

            else:
                print(RED)
                print('***Please Enter Number within range***')    
