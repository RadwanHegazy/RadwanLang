from main import CodeUnit, BaseMethod

class CleanScreen(BaseMethod):
    
    def process (self) :
        # NOTE: compatiable only with windows os
        import os
        os.system('cls')

   
class Write (BaseMethod) : 
    
    def process(self):
        for i in self.get_args() :
            print(i)

    def get_args(self) : 
        line = self.line[self.line.index(':')+1:] # remove @

        # extract method args
        args = []
        lines = line.split(',')
        for line in lines:
            line = line.strip()
            if line.startswith('"') : 
                args.append(line[1:-1])
            else:
                args.append(
                    self.var_manager.get_it(line)
                )


        return args
  

class UserInput(BaseMethod) : 
    
    def process(self):
        var_key , input_txt = self.line.split(':')[-1].split(',')
        data = input(input_txt.strip()[1:-1])
        var_key = var_key.strip()
        return  (var_key, data)
    

class Calc (BaseMethod) : 

    def process(self):
        var_val, operation = self.get_varVal_and_operation()
        set_type = type(self.var_manager.get_it(var_val))
        return var_val, set_type(eval(operation))
    
    def get_varVal_and_operation (self) : 
        var_val, operation = self.line.split(':')[1].split(',')
        return var_val.strip(), operation.strip()
    

class MethodManager (CodeUnit) : 

    __BUILT_IN_METHODS = {
        'cleanScreen' : CleanScreen ,
        'write' : Write,
        'userInput' : UserInput,
        'calc' : Calc
    }

    def __init__(self, line : str, var_manager) -> None:
        self.var_manager = var_manager
        self.args = []
        self.line = line
        if ':' in line :
            self.method_name = self.line[1:self.line.index(':')].strip()
        else:
            self.method_name = line.replace('@',"")



    def response(self) -> None:
        assert self.method_name in self.__BUILT_IN_METHODS, f"Method '{self.method_name}' not defined !"
        method = self.__BUILT_IN_METHODS[self.method_name](self.line, self.var_manager)
        return method.process()
    
