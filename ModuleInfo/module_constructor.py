'''To construct Individual module objects in order to display their data.'''

#? Constructing a class used to create module info objects with it. 

X = ':'*30
RED = '\033[1;31m'
BLUE = '\033[1;34m'
PINK = '\033[1;35m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'

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
        f'''Returns the information about the {self.Name} module.'''
        print(f'{self.Name} Module Info :')
        print('\n')
        exec(f"import {self.name}\
            \nprint({self.name}.__doc__)")

    def classes_list(self) -> None:
        f'''Returns All The Classes defined under {self.Name} Module.'''
        print(f'{self.Name} Module Classes :')
        print('\n')
        for i, j in enumerate(self.data, 1):
            print(i, j[0])

    def class_info(self) -> int:  # function returns an int value
        f'''Returns the information about the Specific Class of {self.Name} module.
        
        Using the input number given by the user.
        '''
        print(X)
        print('Enter Class Number :')
        try: 
            number = input()     
            c = int(number)
            print(X)
            if c in range(1, len(self.data)+1):
                print('Class', self.data[c-1][0], '\n')
                print('Info :\n', self.data[c-1][1], '\n')
                return c
            elif c < 0:
                print(RED)
                print('***Please Enter Only Positive Numbers***')
            else:
                print(RED)
                print('***Please Enter Number within range***')

        except ValueError:
            print(RED)
            print('***Please Enter In Number Format Only***')

        else:
            return c
            # refer : https://stackoverflow.com/questions/20768856/calling-a-variable-from-one-function-to-another-function-in-python 

    def class_method_list(self) -> int:
        f'''Returns All the Methods Under specific Class of {self.Name} Module.'''
        
        # refer : https://devnote.in/how-to-call-one-method-from-another-within-the-same-class-in-python/
        self.classes_list()
        a = self.class_info()
        try:         
            print(X)
            print('Methods under Class %s :' %(self.data[a-1][0]))
            for i, j in enumerate(self.data[a-1][2], 1) : 
                print(i, j)

        except Exception:
            print(RED)
            print(Exception)

        else:
            return a

    def class_method_info(self) -> None:
        f'''Returns the information about the specific method of any class under {self.name} Module.
        
        Using the input number given by the user.    
        '''        
        try:
            d = self.class_method_list()
            print(X)
            print('\nEnter the Method Number :')
            ee = input()
            e = int(ee)
            print(X)
            try:
                if len(self.data[d-1][3])+1 > e > 0:
                    print(self.data[d-1][2][e-1], 'method :\n')  # returns method name
                    print(self.data[d-1][3][e-1])  # returns method info
                else:
                    print(RED)
                    print('***Please Enter A Positive Number within range***') 

            except:
                print(RED)
                print('***Enter Correct Class Number to Proceed***')

        except ValueError:
            print(RED)
            print('\t***Please Enter In Number Format Only***')

    def all_info(self) -> None:  
        f'''Returns All Classes and Methods Under {self.Name} Module along with their information.'''
        
        for i in range(len(self.data)):
            print(X)
            print('Class ', self.data[i][0], '\n')
            print('Info :\n', self.data[i][1])
            print('\n')
            print('Methods Under Class', self.data[i][0], ':\n')

            for e in range(len(self.data[i][2])):
                print('-'*30, '\n', e+1, '.', (self.data[i][2][e]+'()'), 'method :\n')  # returns method name
                print(self.data[i][3][e], '\n')   # returns method info
            print(X)

    def run(self) -> None:
        '''Run'''
        while True :
            print(BLUE)
            print(X)
            print(f'Get {(self.Name)} Module Info')
            print(X)
            print(CYAN)
            print(f' 1 : {self.Name} Module Info           \
                  \n 2 : Classes Under {self.Name} Module  \
                  \n 3 : Get Class Info                    \
                  \n 4 : Get Class Methods List            \
                  \n 5 : Get Class Method Info             \
                  \n 6 : Get All Info                      \
                  \n 7 : Exit \n ')

            input_ = input('Enter Number : ')  
            print(X)

            if input_ == '1':
                self.module_info()

            elif input_ == '2':
                self.classes_list()

            elif input_ == '3':
                self.class_info()

            elif input_ == '4':
                self.class_method_list()

            elif input_ == '5':
                self.class_method_info()

            elif input_ == '6':
                self.all_info()

            elif input_ == '7':
                print(GREEN)
                print('Thank You!')
                break

            elif all(x.isdigit() for x in input_) is False:
                print(RED)
                print('***Please Enter In Number Format***')

            else:
                print(RED)
                print('***Please Enter Number within range***')    

#? For modules with only methods

class Module:
    '''Constructing a 'Module' class. 
    
    With methods defined under it to return the data about the module,and the methods under it.
    Using a combine object(preferably a zip object) containing all the data to be returned using the methods hereby defined.
    '''

    def __init__(self , name: str , data: object) -> None:
        '''Necessary to give the module name and the module data during object instantiation.'''
        self.name = name
        self.Name = name.capitalize()
        self.data = data

    def module_info(self) -> None:
        f'''Returns the information about the {self.Name} module.'''
        print(f'{self.Name} Module Info :')
        print('\n')
        exec(f"import {self.name}\
            \nprint({self.name}.__doc__)")

    def methods_list(self) -> None:
        f'''Returns All The Methods defined under {self.Name} Module In a Systematic manner.'''
        print(f'{self.Name} Methods :\n')
        for i, j in enumerate(self.data, 1):
            print(i, '.', j[0])
            
    def method_info_(self, number: int) -> None:
        f'''Returns the information about the {self.Name} module method.
        
        Using the input number given by the user as an argument while calling the function.
        Seperate Method made for use in the method_info() & all_info() method.
        '''
        self.number = number
        print(self.data[self.number-1][0], 'Method :')
        print(self.data[self.number-1][1])
        print('\n' + '-'*50)

    def method_info(self) -> None:
        '''Return the specific info of a module method enteRED by user, thus calling method_info_() function.'''
        try:        
                number = int(input('Enter Method number : '))
                print(X)
                self.method_info_(number)

        except ValueError:
            print(RED)
            print('\t***Please Enter In Number Format Only***')

        except IndexError:
            print(RED)
            print('\t***Please Enter Number within range***')


    def print_output(self, input_: str) -> str:  # function returns a str value
        import io
        import sys
        old_stdout = sys.stdout 
        new_stdout = io.StringIO() 
        sys.stdout = new_stdout   
        exec(input_)
        output_ = sys.stdout.getvalue().strip()
        sys.stdout = old_stdout     

        return output_ 
        # refer : https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement

    def export_info(self) -> None:
        f'''To create a file with filename enteRED by the user.
        
        A file containing info about the {self.Name} Module and it's Methods.
        '''
        a = 'self.module_info()'
        module_info = self.print_output(a)

        b = 'self.all_info()' 
        methods_info = self.print_output(b)

        file = input('Enter New File name :')
        methods_list = '\n'.join([i[0] for i in self.data])
        x = '\n', ':'*50, '\n'

        with open(f'{file}.txt', 'w') as f :
            f.writelines(x)
            f.write(f'{self.Name} Module')
            f.writelines(x)
            f.write(module_info)
            f.write('\n')
            f.writelines(x)
            f.write(f'{self.Name} Module Methods : \n\n')
            f.write(methods_list)
            f.write('\n')
            f.writelines(x)
            f.write('Methods Info : \n\n')
            f.write(methods_info)

        print(f'Created File : {file}.txt Successfully!')


    def all_info(self) -> None:
        f'''Returns All Methods Under {self.Name} module along with their information.'''
        
        methods_all = tuple(map(lambda a : self.method_info_(a), range(1, len(self.data)+1)))
        print(methods_all[:-len(self.data)])

    def run(self) -> None:
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
                  \n 6 : Exit \n ')

            input_ = input('Enter Number : ')
            print(X)

            if input_ == '1': 
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

            elif all(x.isdigit() for x in input_) is False:
                print(RED)
                print('***Please Enter In Number Format***')

            else:
                print(RED)
                print('***Please Enter Number within range***')  
                
               
