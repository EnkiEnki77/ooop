from typing import Type

# Use type hints on the boundaries of your code, such as function params/returns. Object properties
# (if not inferred through constructor), when you inherit a class.
# Default to not annotating variables, unless the type checker is having a hard time inferring them.
# Examples would be:
# If you assign a variable an empty list, annotate what type the list can contain in the future.
# If you assign a variable None, annotate it with Optional[type it can be]
# When you have complex containers annotate it so the type checker isnt inferring Any.

# You should add a docstring to all functions/methods/classes
class Owner:
    """Object representation of a dog's owner"""

    # You should type hint all method/function params
    def __init__(self, name:str, address:str, contact_number:str):
        """Constructor for the class instance object"""

        self.name = name
        self.address = address
        self.contact_number = contact_number


class Dog:
    """Object representation of a dog"""
    # __init__ is a special method called a constructor. It takes in
    # the arguments
    # passed to the class when its invoked, and is the method that
    # outputs the instance of the class
    # When passing an instance of a class as an argument, it's type is that class.
    # When passing the class in itself you wrap it in type[]
    def __init__(self, name:str, breed:str, owner:Owner):
        """Constructor for the class instance object"""

        # We can attach attributes to the instance using self, which is
        # our reference to the instance.
        # Attributes attached to instance through self are called
        # instance attributes
        self.name = name
        self.breed = breed
        # We can pass in an instance of another class to be used as an
        # instance attribute tying the data together
        self.owner = owner

    # Any methods within the class are automatically attached to the
    # instance.
    def bark(self):
        """Barking behavior of the dog"""

        print("Woof woof!")


owner_1:Owner = Owner("Enki", "316 Dalewood Ave.",
                "540-521-0849")

owner_2:Owner = Owner("Bat", "316 Dalewood Ave.",
                "540-588-0104")

# Whenever we invoke the class it evaluates to a unique instance of
# the class. An instance is an object that follows the blueprint laid
# out by the class, and then is output by the constructor method.
# When you invoke the class youre really invoking the constructor.
dog = Dog("Zach", "Dalmation", owner_1)
# Each time the constructor is invoked, a new execution context is
# added to the call stack with it's own private memory. When that
# individual execution context is traversed entirely by the thread
# it returns the instance, is popped off the callstack, and it's
# private memory removed from RAM. Each time the class is invoked
# and a new execution context is added to the call stack it has
# no ties to the previous execution context, and the data that was
# in it's memory.Therefore, each instance is a unique object with
# it's own individual data
dog_2 = Dog("Bruce", "Husky", owner_2)

# Instance attributes and methods are accessed through dot notation
# print(dog.name)
# print(dog_2.name)
# dog.bark()
# print(dog.owner.name)
# print(dog_2.owner.name)

# We can use the mypy package to do a static type check based on our type hints.

print(type(owner_1))
