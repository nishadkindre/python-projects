'''To construct Individual module objects in order to display their data.'''

X = ':'*30
RED = '\033[1;31m'
BLUE = '\033[1;34m'
PINK = '\033[1;35m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'

#? Constructing a class used to create module info objects with it 
class ModuleC:
    '''Constructing a 'ModuleC' class 
    
    With methods defined under it to return the data about the module,classes under it,methods under the classes.
    Using a combine object(preferably a zip object) containing all the data to be returned using the methods hereby defined.
    '''

    def __init__(self, name: str, data: object) -> None:
        '''Necessary to give the module name and the module data during object instantiation.'''
        self.name = name
        self.Name = name.capitalize()
        self.data = data

    def module_info(self) -> None:
        f'''Returns the information about the {self.Name} Module.'''
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
            c = int(number)
            print(X)
            class_name: str = self.data[c-1][0]
            class_info: str = self.data[c-1][1]

            if c<=0:
                print(RED)
                print('***Please Enter Only Positive Numbers***')
            else: 
                print('Class', class_name, '\n')
                print('Info :\n', class_info, '\n')
                return c
                # refer : https://stackoverflow.com/questions/20768856/calling-a-variable-from-one-function-to-another-function-in-python 

        except ValueError:
            print(RED)
            print('***Please Enter In Number Format Only***')

        except IndexError:
            print(RED)
            print('***Please Enter Number within range***')

    def class_methods_list(self) -> int:
        '''Returns All the Methods Under specific Class of the Module.'''
        self.classes_list()
        a: int = self.class_info()
        class_name: str = self.data[a-1][0]
        class_methods: tuple = self.data[a-1][2]

        try:         
            print(X)
            print(f'Methods under Class {class_name} :')
            for i, j in enumerate(class_methods, 1) : 
                print(i, j)
                
        except Exception:
            print('.')  # prints when an exception occurs in the method called
        else:
            return a

    def class_method_info(self) -> None:
        '''Returns the information about the specific method of any class under the Module.
        
        Using the input number given by the user.    
        '''        
        try:
            d: int = self.class_methods_list()
            print(X)
            print('\nEnter the Method Number :')
            number = input()
            e = int(number)
            print(X)

            methods_info_list: tuple = self.data[d-1][3]
            method_name: str = self.data[d-1][2][e-1]
            method_info: str = methods_info_list[e-1]

            if e not in range(1, len(methods_info_list)+1):
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

            for e in range(len(class_methods)):
                method_name: str = self.data[i][2][e] + '()'
                method_info: str = self.data[i][3][e]
                print(x)
                print(e+1, '.', method_name, 'method :\n')
                print(method_info, '\n')
            print(X)

    def print_output(self, input_: str) -> str:  # function returns a str value
        '''Helper Method.

        >>> Return the output of an input(a function in our case) taken as an argument.
        >>> For special purpose of printing output in a text file.

        Special Method made for use in the exprt_info() method of both classes.
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

    def export_info(self):
        '''To create a file with filename entered by the user.
        
        A file containing info about the  Module and it's Methods.
        '''       
        a = 'self.all_info()' 
        all_info = self.print_output(a)
        file = input('Enter New File name :')
        with open(f'{file}.txt', 'w') as f :
            f.write(all_info)
            
        print(f'Created File : {file}.txt Successfully!')

    def run(self) -> None:
        '''Run'''
        while True :
            print(BLUE)
            print(X)
            print(f'Get {self.Name} Module Info')
            print(X)
            print(CYAN)
            print(f' 1 : {self.Name} Module Info           \
                  \n 2 : Classes Under {self.Name} Module  \
                  \n 3 : Get Class Info                    \
                  \n 4 : Get Class Methods List            \
                  \n 5 : Get Class Method Info             \
                  \n 6 : Get All Info                      \
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

#? For modules with only methods
class Module(ModuleC):
    
    '''Constructing a 'Module' class. 
    
    With methods defined under it to return the data about the module,and the methods under it.
    Using a combine object(preferably a zip object) containing all the data to be returned using the methods hereby defined.
    '''

    def methods_list(self) -> None:
        '''Returns All The Methods defined under the Module In a Systematic manner.'''
        print(f'{self.Name} Methods :\n')
        for i, j in enumerate(self.data, 1):
            print(i, j[0])
            
    def method_info_(self, number: int) -> None:
        '''Helper Method.

        >>> Returns the information about the specific Module method.
        >>> Using the input number given by the user as an argument while calling the function.

        Special Method made for use in the method_info() & all_info() method.
        '''
        x: str = '\n' + '-'*50
        self.number = number
        method_name: str = self.data[self.number-1][0]
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
        methods_all = tuple(map(lambda a: self.method_info_(a), range(1, len(self.data)+1)))
        print(methods_all[:-len(self.data)])

    def export_info(self) -> None:
        '''To create a file with filename entered by the user.
        
        A file containing info about the Module and it's Methods.
        '''
        x = '\n', ':'*50, '\n'
        a = 'self.module_info()'
        b = 'self.all_info()' 

        module_info = self.print_output(a)
        methods_info = self.print_output(b)
        methods_list = '\n'.join([i[0] for i in self.data])

        file = input('Enter New File name :')
        with open(f'{file}.txt', 'w') as f :
            f.writelines(x)
            f.write(f'{self.Name} Module')
            f.writelines(x)
            f.write(module_info)
            f.write('\n')
            f.writelines(x)
            f.write(f'{self.Name} Module Methods :')
            f.write('\n\n')
            f.write(methods_list)
            f.write('\n')
            f.writelines(x)
            f.write('Methods Info :')
            f.write('\n\n')
            f.write(methods_info)

        print(f'Created File : {file}.txt Successfully!')

    def run(self) -> None:
        '''Run'''
        while True:
            print(BLUE)
            print(X)
            print(f'Get {self.Name} Module Info')
            print(X)
            print(CYAN)
            print(f' 1 : {self.Name} Module info          \
                  \n 2 : Method List                      \
                  \n 3 : Method Info                      \
                  \n 4 : Get All Methods Info             \
                  \n 5 : Export All Info To a Text File   \
                  \n 6 : Exit \n')

            input_ = input('Enter Number : ')
            print(X)

            if all(x.isdigit() for x in input_) is False:
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
