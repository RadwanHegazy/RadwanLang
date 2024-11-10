from var_manager import VariableManager


class CodeParser:

    __vars = VariableManager()
    __line = 0
    

    def __init__(self, code_lines:list[str]) -> None:
        code_lines = self.__remove_comments(code_lines)
        
        for line in code_lines : 
            
            if line.startswith(self.__vars.get_types_keys()) and ":" in line : 
                self.__parse_variable(line)

            self.__line += 1
            

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
    
    def __remove_comments (self, code_lines) :
        new_code_lines = []

        for code in code_lines :
            if not code.startswith('# ') and len(code) != 0:
                new_code_lines.append(code)
        
        return new_code_lines