from typing import Optional, Sequence

# If we want to give a type of a nested list we would do the following:
x: list[list[int]] = [[17]]

# To annotate for a dict with one value we pass the dict a type for the key and value
y: dict[str, int] = {"age": 4}

# To annotate for a dict with potentially multiple values we pass the dict a type for the key and one
# value OR another
z: dict[str, int | str] = {"age": 4, "name": "Enki"}

# We pretty much dont need to annotate variables, because the checker is pretty good at inferring.
# Just make sure youre checking what its inference is and annotating as needed. For empty lists
# you may need to annotate what it should be when values are added. And when making a variable
# optional with None annotate with Optional

# We want to initialize list as empty, but enforce that only one type should be appended to it later.
b:list[int] = []

# We dont want just None type here because we're trying to say its empty at the moment but it
# wont be later
Name:Optional[str] = None


# When you have complicated types it may be more readable to assign them to a type alias
Vector = list[int]

my_list: Vector = [6, 6]


# If you want to accept any sequence (list, tuple, dict, etc.) use the Sequence type
# Whenever we use optional params they should be typed as optional
def my_function(seq: Sequence, output:Optional[bool]=False) -> None:
     pass