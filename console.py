#!/usr/bin/python3


"""Console 0.0.1"""


import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""

    prompt = '(hbnb) '
    cls = ["BaseModel", "User", "State"]
    file = None

    def do_create(self, arg):
        """Creates a new instance of "BaseModel", saves it
           (in the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg in self.cls:
            obj = eval(arg)()
            eval(arg).save(obj)
            print(obj.id)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
