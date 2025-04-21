from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def eat(self):
        ...

    def fly(self):
        print("I believe I can fly!")
    
    @abstractmethod
    def make_noise(self):
        ...

    def swim(self):
        ...
