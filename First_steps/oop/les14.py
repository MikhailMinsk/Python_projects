class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)


c = Celsius
c.temperature = 2
print(c.to_fahrenheit)


class Temperature(object):
    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) / 1.8

    def __str__(self):
        return 'Celsius: {:g}\nFahrenheit: {:g}\n'.format(
            self.celsius, self.fahrenheit)


def main():
    temperature = Temperature(24)
    print(temperature)

    temperature.celsius = 10
    print(temperature)

    temperature.fahrenheit = 100
    print(temperature)


if __name__ == '__main__':
    main()
