import sys, os
from parser import CodeParser


class Interpreter :
    """
    Read and implement the code
    """
    def __init__(self, file_path) -> None:
        self.file_path = file_path

        current_directory = os.path.dirname(os.path.abspath(__file__))
        filename = file_path
        file_path = os.path.join(current_directory,filename)

        if file_path.endswith('.radwan') : 
            code = open(file_path, 'r')
            self.code_lines = code.read().split('\n')
        else:
            raise Exception("Invalid file extension name")
   
    def run (self) : 
        """
        Run the list of code lines
        """
        CodeParser(self.code_lines)

if __name__ == "__main__" : 
    file_path = sys.argv[1:]
    if file_path:
        file_path = file_path[0]
        interpreter = Interpreter(file_path)
        interpreter.run()
    else:    
        print('[!] Please Insert file path.')
