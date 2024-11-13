from manager import MemoryManager
from dispatcher import Dispatcher

class CodeParser:

    __memory_manager = MemoryManager()
    __line = 0
    
    def __init__(self, code_lines:list[str]) -> None:
        
        for line in code_lines : 
            self.__line += 1

            # ignore the comments lines 
            if line.startswith('#') or len(line) == 0:
                continue
            
            # save the instractions to memory and implement it,
            # The write new output to the memory
            dis = Dispatcher(line, self.__memory_manager, self.__line)
            self.__memory_manager = dis.response()


        