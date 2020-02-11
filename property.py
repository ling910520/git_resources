class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    @property
    def temperature(self):
        print("Getting value")
        return self._temperature
    @temperature.setter
    def temperature(self,value):
        if(value<-273):
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
    def print_module(self):
        print(self.__module__ + "." + self.__class__.__name__)
c=Celsius(37)
c.print_module()
c.temperature = 37
c.temperature =37
c.temperature
c.temperature = 37