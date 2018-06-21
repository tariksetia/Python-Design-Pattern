from abc import ABCMeta,abstractmethod
import time

### Implementation of Design Pattern As discussed in Head First Design Pattern
class IObservable(metaclass=ABCMeta):
    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass
    
    @abstractmethod
    def notify(self):
        pass


class IObserver(metaclass=ABCMeta): 
    
    @abstractmethod
    def update(self):
        pass


class IDisplay(metaclass=ABCMeta):
    
    @abstractmethod
    def display(self):
        pass


class WeatherStation(IObservable): #Concrete Observable
    observer_list = []
    __temprature = None
    def attach(self,observer):
        if isinstance(observer,IObserver) and observer not in self.observer_list:
            self.observer_list.append(observer)
    
    def detach(self,observer):
        try:
            observer_list.pop(observer)
        except ValueError:
            print("Observer Not Found")
    
    def notify(self):
        for observer in self.observer_list:
            observer.update()
    
    # Other Methods to get and change state
    @property
    def temprature(self): #celcius temprature
        return self.__temprature if self.__temprature else None
    
    @temprature.setter
    def temprature(self,value):
        self.__temprature = value #Celecius value
        self.notify()
        
        
class KelvinDisplay(IObserver,IDisplay):

    def __init__(self,observable): #Observable is Weather stattion
        self.__observable = observable
        observable.attach(self)
        self.display()

    def update(self):
        self.display()
    
    def display(self):
        temprature = self.__observable.temprature

        if not temprature:
            print('Temprature Not Set')
            return

        kelvin = temprature + 273
        print("Temprature = {} K".format(kelvin))


class FahrenheitDisplay(IObserver,IDisplay):
    
    def __init__(self,observable): #Observable is Weather stattion
        self.__observable = observable
        observable.attach(self)
        self.display()

    def update(self):
        self.display()
    
    def display(self):
        temprature = self.__observable.temprature

        if not temprature:
            print('Temprature Not Set')
            return
            
        fah = (9/5) * temprature + 32
        print("Temprature = {} F".format(fah))


if __name__ == '__main__':
    
    weather_station = WeatherStation()
    fahren_display = FahrenheitDisplay(weather_station)
    kelvin_display = KelvinDisplay(weather_station)
    weather_station.temprature = 32
    while weather_station.temprature < 40:
        weather_station.temprature += 1
        time.sleep(1)