from abc import ABCMeta, abstractmethod
from typing import Any

class BaseManager(metaclass=ABCMeta) : 

    @abstractmethod
    def get_it(self, key, val) : ...

    @abstractmethod
    def set_it(self, key) : ...

class MemoryManager : 
    
    __VARS : dict[object, Any] = {}

    def set_it (self, key, val) -> None:
        self.__VARS[key] = val
    
    def get_it (self, key) :
        return self.__VARS.get(key, None) 