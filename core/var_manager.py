

class VariableManager : 
    __TYPE = {
        's' : str,
        'i' : int,
        'f' : float,
        'b' : bool
    }
    __VARS = {}


    def set_var (self, _type, key, val=None) -> None:
        assert _type in self.__TYPE.keys(), f"TypeError: Invalid data type '{_type}' "
        
        if val :
            try :
                self.__TYPE[_type](val)
            except ValueError : 
                raise ValueError(f"Invalid data value '{val}' to variable '{key}' with data type '{_type}' ")

        self.__VARS[key] = (
            self.__TYPE[_type],
            val
        )
        
    def get_var (self, key) :
        return self.__VARS.get(key, None) 
        
    def get_types_keys(self) : 
        return tuple(self.__TYPE.keys())

