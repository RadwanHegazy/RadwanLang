from built_in_methods import cleanScreen, write, userInput

class UserDefineMethod:

    def __init__(self, method_code, parser) -> None:
        self.method_code = method_code
        self.parser = parser

    def call(self) : 
        return self.parser(self.method_code)
    
class MethodManager :
    
    __BUILT_IN = {
        'cleanScreen' : cleanScreen,
        'write' : write,
        'userInput' : userInput,
    }

    __USER_DEFINE : dict[str, UserDefineMethod] = {}

    def call (self, method_name : str, args : list = []) : 
        method_name = method_name.strip()

        built_in_method = self.__BUILT_IN.get(method_name, None)
        user_define_method = self.__USER_DEFINE.get(method_name, None)

        if built_in_method is None and user_define_method is None: 
            raise Exception(f"method '{method_name}' not found !")
        
        if user_define_method:
            return self.__call_user_define_method(method_name)

        if any(args):
            response  = self.__BUILT_IN[method_name](*args)
        else:
            response = self.__BUILT_IN[method_name]()

        return response
        
    def define_method(self, method_name, method_code, CodeParser) :
        self.__USER_DEFINE[method_name] = UserDefineMethod(method_code, CodeParser)
    
    def built_ins_method_names(self) : 
        return self.__BUILT_IN.keys()

    def __call_user_define_method (self, name) :
        response = self.__USER_DEFINE.get(name).call()
        return response