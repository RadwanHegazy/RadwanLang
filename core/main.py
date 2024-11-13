from abc import ABCMeta, abstractmethod

class CodeUnit(metaclass=ABCMeta):
    
    def __init__(self, line) -> None:
        self.line = line

    @abstractmethod
    def response(self) -> tuple : ... # ( key, val )


class MainDispatcher(metaclass=ABCMeta):

    @abstractmethod
    def response (self) : ...


class BaseMethod (metaclass=ABCMeta) : 
    
    def __init__(self, line=None, var_manager=None) -> None:
        self.line = line
        self.var_manager = var_manager
        
    @abstractmethod
    def process(self) : ...


