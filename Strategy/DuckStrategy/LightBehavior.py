from .ILightBehavior import ILightBehavior
class ButtonLightBehavior(ILightBehavior):
    def turn_on(self):
        print('Button On')
    
    def turn_off(self):
        print('Button Off')