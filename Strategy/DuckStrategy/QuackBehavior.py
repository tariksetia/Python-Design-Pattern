from .IQuackBehavior import IQuackBehavior

class CalmQuackBehavior(IQuackBehavior):
    def quack(self):
        print('quack! I am a Calm Duck')

class LoudDuckBehavior(IQuackBehavior):
    def quack(self):
        print('QUACK!! QUACK!! I am a LOUD Duck')