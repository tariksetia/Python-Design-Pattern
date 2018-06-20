from strategy import fast_fly_strategy, slow_fly_strategy, calm_quack_strategy, loud_duck_strategy ,button_turn_on_strategy, button_turn_off_strategy
from types import MethodType


class Duck():
    def __init__(self, fly_strategy=None, quack_strategy=None, light_turn_on_strategy=None, light_turn_off_stategy=None):
        if fly_strategy is not None: self.fly = MethodType(fly_strategy,self) 
        if quack_strategy is not None: self.quack = MethodType(quack_strategy,self) 
        if light_turn_off_stategy is not None: self.turn_on = MethodType(light_turn_on_strategy,self) 
        if light_turn_off_stategy is not None: self.turn_off = MethodType(light_turn_off_stategy,self) 
        
    def fly(self):
        raise NotImplemented('Method does not exist')
    
    def quack(self):
        raise NotImplemented('Method does not exist')
    
    def turn_off(self):
        raise NotImplemented('Method does not exist')
    
    def turn_on(self):
        raise NotImplemented('Method does not exist')


if __name__ == '__main__':
    toy_duck = Duck(quack_strategy=calm_quack_strategy)

    robo_duck = Duck(fly_strategy=slow_fly_strategy, quack_strategy=loud_duck_strategy, light_turn_on_strategy=button_turn_on_strategy, light_turn_off_stategy=button_turn_off_strategy)

    city_duck = Duck(fly_strategy=fast_fly_strategy,quack_strategy=loud_duck_strategy)