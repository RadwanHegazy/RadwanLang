from built_in_methods import cleanScreen, write

class MethodManager :
    
    
    __BUILT_IN = {
        'cleanScreen' : cleanScreen,
        'write' : write
    }

    __USER_DEFINE = {}

    def call (self, method_name : str, args : list = []) : 
        method_name = method_name.strip()
        assert method_name in self.__BUILT_IN.keys(), f"method '{method_name}' not found !"
        if any(args):
            self.__BUILT_IN[method_name](*args)
        else:
            self.__BUILT_IN[method_name]()


        