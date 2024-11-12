from var_manager import VariableManager
from method_manager import MethodManager

class CodeParser:

    __vars = VariableManager()
    __methods = MethodManager()
    __line = 0
    

    def __init__(self, code_lines:list[str]) -> None:
        for line in code_lines : 

            # work with comments
            if line.startswith('#') or len(line) == 0:
                continue
            
            # work with methods
            if line.startswith('@') : 
                method_name, *more = line[1:].split(':')
                if more : 
                    args = self.__parse_method_args(more[0])
                    args.append(self.__vars)
                    response = self.__methods.call(method_name, args)
                else:
                    response = self.__methods.call(method_name)
                
                # write update on variables on the method response
                if response:
                    self.__vars = response

            # work with variables
            if line.startswith(self.__vars.get_types_keys()) and ":" in line : 
                self.__parse_variable(line)

            self.__line += 1
            

    def __parse_method_args (self, args_txt) :
        func_vars = args_txt.strip().split(',')
        args = []
        for v in func_vars : 
            v = v.strip()
            if v.startswith('"') and v.endswith('"') : 
                args.append(v)
            else:
                var_value = self.__vars.get_var(v)
                if var_value:
                    _type, val, *other = var_value
                    value = _type(val)
                else:
                    raise ValueError(f"Variable '{v}' not declared ")
                # args.append(value)
                args.append(var_value)

        return args

    def __parse_variable (self, line:str) : 
        if ":" not in line:
            self.__push_error("your forget to add ':' to set the type of yor var.")
        
        var_type, var = line.split(':')
        
        if '=' in var :
            var_key, var_val = var.split('=')
        else:
            var_key, var_val = var, None
 
        self.__vars.set_var(
            var_type,
            var_key.strip(),
            var_val
        )


    def __push_error(self, error_text) : 
        raise Exception(f"error at line {self.__line} : ", error_text)
