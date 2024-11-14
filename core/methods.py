from main import BaseMethod

class CleanScreen(BaseMethod):
    
    def process (self) :
        # NOTE: compatiable only with windows os
        import os
        os.system('cls')

   
class Write (BaseMethod) : 
    
    def process(self):
        for i in self.get_args() :
            print(i)

    def get_args(self) : 
        line = self.line[self.line.index(':')+1:] # remove @

        # extract method args
        args = []
        lines = line.split(',')
        for line in lines:
            line = line.strip()
            if line.startswith('"') : 
                args.append(line[1:-1])
            else:
                args.append(
                    self.var_manager.get_it(line)
                )


        return args
  

class UserInput(BaseMethod) : 
    
    def process(self):
        var_key , input_txt = self.line.split(':')[-1].split(',')
        data = input(input_txt.strip()[1:-1])
        var_key = var_key.strip()
        return  (var_key, data)
    

class Calc (BaseMethod) : 

    def process(self):
        var_val, operation = self.get_varVal_and_operation()
        set_type = type(self.var_manager.get_it(var_val))
        return var_val, set_type(eval(operation))
    
    def get_varVal_and_operation (self) : 
        var_val, operation = self.line.split(':')[1].split(',')
        return var_val.strip(), operation.strip()
    
class If (BaseMethod) : 


    def process(self):
        is_true, result = self.extract()
        if is_true:
            print(result)
        return None
    
    def extract(self) : 
        if '->' not in self.line:
            raise Exception("you forget -> in the condition !")
        
        condition, output = self.line.split('->')
        
        output = output.strip()
        if output.startswith('"'):
            output = output[1:-1]
        else:
            self.var_manager.get_it(output)

        if "==" in condition:
            return (
                self.equals(
                    *self.get_r_l(condition, '==')
                    ),
                    output
                )
        elif "!=" in condition:
            return (
                self.not_equals(
                    *self.get_r_l(condition, '!=')
                    ),
                    output
                )
        else:
            raise Exception("Invalid condition operation")
        
    def equals(self, r, l) :
        return r == l

    def not_equals(self, r, l) : 
        return r != l

    def get_r_l (self, condition ,operation) : 
        r,l = condition.split(operation)
        r,l = r.split(":")[1].strip(), l.strip()
        if r.startswith('"'):
            r = r[1:-1]
        else:
            r = self.var_manager.get_it(r)
            if r:
                r = int(r) if r.isnumeric() else r

        if l.startswith('"') : 
            l = l[1:-1]
        else:
            if l.isnumeric() :
                l = int(l)
            else:
                l = self.var_manager.get_it(l)
                
        return (r, l)
    
