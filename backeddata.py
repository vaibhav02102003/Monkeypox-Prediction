from django.contrib.auth.models import User
import numpy as np

def some_function():
    """Example function to demonstrate fixing formatting issues."""
    print("Hello, world!")

class ExampleClass:
    """Example class to demonstrate correct spacing."""

    def __init__(self, value):
        self.value = value

    def display(self):
        """Displays the value."""
        print(self.value)

long_string = (
    "This is a very long string that exceeds the 79-character limit, so "
    "we split it into multiple lines for readability."
)

def another_function():
    """Another function example."""
    print("Another function.")

example_dict = {
    "key1": "This is a long dictionary entry that is split "
            "across multiple lines for readability.",
    "key2": "Another long dictionary entry that is formatted correctly."
}

class AnotherClass:
    """Another example class."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        """Greets the user."""
        print(f"Hello, {self.name}!")

if __name__ == "__main__":
    obj = ExampleClass("Sample")
    obj.display()
    another_function()
    print(long_string)
