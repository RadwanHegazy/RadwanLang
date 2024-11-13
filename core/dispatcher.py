from main import MainDispatcher
from variables import (
    BoolVar,
    FloatVar,
    IntegerVar,
    StringVar,
)

from methods import MethodManager

class Dispatcher (MainDispatcher):

    __REGISTERD = {
        's' : StringVar,
        'i' : IntegerVar,
        'f' : FloatVar,
        'b' : BoolVar,
        "@" : MethodManager
    }

    def __init__(self, code_line : str, manager, line_number : int) -> None:
        key = code_line[0]
        is_method = key == "@"
        self.manager = manager

        if not is_method : 
            assert key in self.__REGISTERD.keys(), f"error on line {line_number} -> {code_line}"
            output = self.__REGISTERD[key](code_line)
        else:
            output = self.__REGISTERD[key](code_line, self.manager)

        self.__output = output
    
    def response (self) : 
        response = self.__output.response()
        if response :
            key, val = response
            self.manager.set_it(key, val)
        return self.manager