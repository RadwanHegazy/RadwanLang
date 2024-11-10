import sys
from parser import CodeParser

class Interpreter :
    __code_lines = [] 

    def run_lines (self, code_lines) : 
        CodeParser(code_lines)
            
    def run_line (self, code) : 
        self.__code_lines.append(code)
        try :
            CodeParser(self.__code_lines)
        except Exception as error:
            print("Error: ", error)
            self.__code_lines.pop()


if __name__ == "__main__" : 
    interpreter = Interpreter()
    file_path = sys.argv[1:]
    
    if file_path:
        file_path = file_path[0]
        file_path = sys.path[0] + '\\' + file_path
        if file_path.endswith('.radwan') : 
            code = open(file_path, 'r')
            code_lines = code.read().split('\n')
            interpreter.run_lines(code_lines)
        else:
            raise Exception("Invalid file extension name")
    else:    
        while True :
            try : 
                code = input('RadwanLang > ')
                interpreter.run_line(code)
            except KeyboardInterrupt :
                break