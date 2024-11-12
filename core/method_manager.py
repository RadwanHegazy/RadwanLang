from built_in_methods import cleanScreen, write, userInput

class MethodManager :
    
    
    __BUILT_IN = {
        'cleanScreen' : cleanScreen,
        'write' : write,
        'userInput' : userInput
    }

    __USER_DEFINE = {}

    def call (self, method_name : str, args : list = []) : 
        method_name = method_name.strip()
        assert method_name in self.__BUILT_IN.keys(), f"method '{method_name}' not found !"
        if any(args):
            response  = self.__BUILT_IN[method_name](*args)
        else:
            response = self.__BUILT_IN[method_name]()

        return response

        