import sys
from parser import CodeParser

class Interpreter :
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        file_path = sys.path[0] + '..\\' + file_path
        if file_path.endswith('.radwan') : 
            code = open(file_path, 'r')
            self.code_lines = code.read().split('\n')
        else:
            raise Exception("Invalid file extension name")
   
    def run (self) : 
        CodeParser(self.code_lines)

if __name__ == "__main__" : 
    file_path = sys.argv[1:]
    if file_path:
        file_path = file_path[0]
        interpreter = Interpreter(file_path)
        interpreter.run()
    else:    
        print('[!] Please Insert file path.')
