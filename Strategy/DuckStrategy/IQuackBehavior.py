from abc import ABCMeta,abstractmethod

class IQuackBehavior(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        '''the Duck Quak Behaviour Goes Here'''
        pass