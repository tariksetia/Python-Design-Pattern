from abc import ABCMeta, abstractmethod

class ILightBehavior(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self):
        ''' Lights Turn On Algorithm'''
        pass
    
    @abstractmethod
    def turn_off(self):
        ''' Lights TurnOff Alrogrithm'''
        pass