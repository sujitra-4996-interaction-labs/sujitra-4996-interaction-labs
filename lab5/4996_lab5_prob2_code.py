from abc import ABC, abstractmethod

class Animal(ABC):
    """
    This class represents an abstract animal.
    """

    @abstractmethod
    def move(self):
        """
        An abstract method to define how an animal moves.
        """
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

if __name__ == "__main__":
    print("prob2.py: This file illustrates the usage of an abstract class and DocStrings\n")
    
    print("Class animal is an abstract class that has abstract method move")
    print("Method move is an abstract method of an abstract class Animal")
    
    print("=== Below is the output of the code ===")
    
    human = Human()
    human.move()

    snake = Snake()
    snake.move()

    dog = Dog()
    dog.move()
