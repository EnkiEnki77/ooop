class Person:
    """Object representing a person"""

    def __init__(self, name: str, age: int) -> None:
        """Constructor for the class instance"""

        self.name = name
        self.age = age

    # Passing self to each method gives access to the current instances data.
    def greet(self) -> None:
        """Greeting behavior from person, declaring name and age"""

        print(f"Hello, I'm {self.name}. I'm {self.age} years old!")


enki = Person("Enki", 26)
enki.greet()