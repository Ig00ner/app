"""class Person:       # определение класса Person
     def say_hello(self):
        print("Hello")
 
tom = Person()
tom.say_hello()    # Hello
"""

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(self)

    def __str__(self):
        return f""" Автомобиль:
    Марка: {self.brand}
    Модель: {self.model}
    Год: {self.year}"""


def main():
    car = Car("BMW", "740", "2004")
    car.display_info() # Магия :-)

if __name__ == '__main__':
    main()