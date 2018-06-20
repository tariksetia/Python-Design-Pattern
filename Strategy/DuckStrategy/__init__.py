from .FlyBehavior import SlowFlyBehavior, FastFlyBehavior
from .QuackBehavior import CalmQuackBehavior, LoudDuckBehavior
from .LightBehavior import ButtonLightBehavior

button_light_behavior = ButtonLightBehavior()
fast_flying_duck = FastFlyBehavior()
slow_flying_duck = SlowFlyBehavior()
calm_duck = CalmQuackBehavior()
loud_duck = LoudDuckBehavior()