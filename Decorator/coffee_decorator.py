from abc import ABCMeta, abstractmethod

class Beverage(metaclass=ABCMeta):
    
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

class AddOnDecorator(Beverage,metaclass=ABCMeta):
    def __str__(self):
        if isinstance(self.beverage, AddOnDecorator):
            return "{}, {}".format(str(self.beverage),self.add_on_name)    
        if isinstance(self.beverage, Beverage):
            return "{} with {}".format(str(self.beverage), self.add_on_name)

class Espresso(Beverage): #Concrete Beverage Class
    def __init__(self):
        self.coffee_name = 'Espresso'

    def cost(self):
        return 2.0
    
    def __str__(self):
        return "{} Coffee".format(self.coffee_name)    

class CaramelAddOn(AddOnDecorator): #Concrete AddOn Class

    def __init__(self,beverage):
        self.beverage = beverage
        self.add_on_name = 'Caramel'
    
    def cost(self):
        return self.beverage.cost() + 1.0

class ChocolateAddOn(AddOnDecorator): #Concorete AddOn Class
    
    def __init__(self,beverage):
        self.beverage = beverage
        self.add_on_name = 'Chocolate'
    
    def cost(self):
        return self.beverage.cost() + 1.0 
    
if __name__ == '__main__':
    coffees = [
        Espresso(), 
        CaramelAddOn(Espresso()), 
        ChocolateAddOn(Espresso()), 
        ChocolateAddOn(CaramelAddOn(Espresso())), 
        CaramelAddOn(ChocolateAddOn(Espresso()))
        ]
    for coffee in coffees:
        print("{} = {}".format(str(coffee),str(coffee.cost())))
