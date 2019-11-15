# "__init__" is a reseved method in python classes.
# It is called as a constructor in object oriented terminology.
# This method is called when an object is created from a class and
# it allows the class to initialize the attributes of the class.
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """"Initialize name and age atributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in reponse to a command."""
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        """"Simulate rolling over in respone to a command"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('Bootha', 7)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


