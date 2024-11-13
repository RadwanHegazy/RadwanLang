from main import CodeUnit


class VarUnit (CodeUnit) : 
    
    __VARS = {
        's' : str,
        'i' : int,
        'f' : float,
        'b' : bool
    }

    def var_spliiter(self) : 
        val = []
        txt = ""
        idx = 0
        while idx <= len(self.line) :
            txt += self.line[idx]
            if self.line[idx+ 1]  == '=' : 
                val.append(txt.strip())
                val.append(self.line[idx+2:].strip())
                break
            idx += 1
        return val

    def get_value (self, text_val) : 
        return self.__VARS.get(text_val)
    
    def extractor (self) -> tuple :
        """Extract variable details the plaintext line  

        Returns:
            tuple: (var_type, var_key, var_value)
        """
        if '=' in self.line : 
            var_details, var_value = self.var_spliiter()
            var_type, var_key = var_details.split(':')
        else:
            var_type, var_key = self.line.split(':')

        return (
            self.get_value(var_type.strip()),
            var_key.strip(),
            var_value
        )
    
class StringVar (VarUnit) :

    def response(self):
        _type, key, value = self.extractor()
        value = value[1:-1]
        return ( 
            key,
            value
        )


class IntegerVar (VarUnit) : 
    
    def response(self):
        _type, key, value = self.extractor()
        value = int(value)
        return ( 
            key,
            value
        )


class FloatVar (VarUnit) : 

    def response(self):
        _type, key, value = self.extractor()
        value = float(value)
        return ( 
            key,
            value
        )



class BoolVar (VarUnit) : 

    def response(self) -> tuple:
        _type, key, value = self.extractor()
        value = bool(int(value))
        return ( 
            key,
            value
        )
    
