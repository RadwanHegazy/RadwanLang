

class VariableManager : 
    __TYPE = {
        's' : str,
        'i' : int,
        'f' : float,
        'b' : bool
    }
    
    __RTYPE = {
        str : "s",
        int : "i",
        float : "f",
        bool : 'b',
    }
    
    __VARS = {}

    def set_var (self, _type, key, val=None) -> None:
        assert _type in self.__TYPE.keys(), f"TypeError: Invalid data type '{_type}' "
        
        if val :
            try :
                var_type = self.__TYPE[_type](val)
            except ValueError : 
                raise ValueError(f"Invalid data value '{val}' to variable '{key}' with data type '{_type}' ")


        self.__VARS[key] = (
            self.__TYPE[_type],
            val,
            key
        )
        
    def get_var (self, key) :
        return self.__VARS.get(key, None) 
        
    def get_types_keys(self) : 
        return tuple(self.__TYPE.keys())

    def get_rtype(self, val) : 
        return self.__RTYPE[val]