from abc import ABCMeta, abstractmethod

class IFlyBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        '''Ducks Fly Algorithm'''
        pass