from .IFlyBehavior import IFlyBehaviour

class SlowFlyBehavior(IFlyBehaviour):
    def fly(self):
        print("I am a slow flying Duck")

class FastFlyBehavior(IFlyBehaviour):
    def fly(self):
        print("I am a turbojet Duck")