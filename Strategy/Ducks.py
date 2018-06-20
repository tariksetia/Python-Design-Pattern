from DuckStrategy import button_light_behavior, fast_flying_duck, slow_flying_duck, calm_duck, loud_duck

class Duck():
    def __init__(self, fly_behavior, quack_behavior, light_behavior):
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior
        self._light_behavior = light_behavior
    
    def fly(self):
        self._fly_behavior.fly()
    
    def quack(self):
        self._quack_behavior.quack()

    def turn_on(self):
        self._light_behavior.turn_on()
    
    def turn_off(self):
        self._light_behavior.turn_off()


class CityDuck(Duck):
    def __init__(self):
        super().__init__(fast_flying_duck, loud_duck, None)

    def whoami(self):
        print('I am a city duck')

class VillageDuck(Duck):
    def __init__(self):
        super().__init__(slow_flying_duck, calm_duck, None)
    
    def whoami(self):
        print('I am a Village Duck')

class ToyDuck(Duck):
    def __init__(self):
        super().__init__(None, calm_duck, None)

    def whoami(self):
        print('I am a Toy Duck')
    
class RobotDuck(Duck):
    def __init__(self):
        super().__init__(fast_flying_duck, loud_duck, button_light_behavior)

    def whoami(self):
        print('I am a Robot Duck')