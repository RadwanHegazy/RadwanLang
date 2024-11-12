import sys
from parser import CodeParser

class Interpreter :

    def run (self, code_lines) : 
        CodeParser(code_lines)
            

if __name__ == "__main__" : 
    interpreter = Interpreter()
    file_path = sys.argv[1:]
    
    if file_path:
        file_path = file_path[0]
        file_path = sys.path[0] + '\\' + file_path
        if file_path.endswith('.radwan') : 
            code = open(file_path, 'r')
            code_lines = code.read().split('\n')
            interpreter.run(code_lines)
        else:
            raise Exception("Invalid file extension name")
    else:    
        print('[!] Please Insert file path.')
