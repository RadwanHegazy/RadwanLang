from methods import *
from main import CodeUnit

class MethodManager (CodeUnit) : 
    """
    Method Manager for implement built-in methods
    """
    __BUILT_IN_METHODS = {
        'cleanScreen' : CleanScreen ,
        'write' : Write,
        'userInput' : UserInput,
        'calc' : Calc,
        'if' : If
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
        """
        Method Response
        """
        assert self.method_name in self.__BUILT_IN_METHODS, f"Method '{self.method_name}' not defined !"
        method = self.__BUILT_IN_METHODS[self.method_name](self.line, self.var_manager)
        return method.process()
    
