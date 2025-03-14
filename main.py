class Dog:
    # __init__ is a special method called a constructor. It takes in the arguments
    # passed to the class when its invoked, and is the method that outputs the
    # instance of the class
    def __init__(self, name, breed, owner):
        # We can attach attributes to the instance using self, which is our
        # reference to the instance.
        # Attributes attached to instance through self are called instance attributes
        self.name = name
        self.breed = breed
        # We can pass in an instance of another class to be used as an instance attribute
        # tieing the data together
        self.owner = owner

    # Any methods within the class are automatically attached to the instance.
    def bark(self):
        print("Woof woof!")


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number



owner_1 = Owner("Enki", "316 Dalewood Ave.", "540-521-0849")
owner_2 = Owner("Bat", "316 Dalewood Ave.", "540-588-0104")

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
print(dog.name)
print(dog_2.name)
dog.bark()
print(dog.owner.name)
print(dog_2.owner.name)
