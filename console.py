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

    def do_show(sefl, arg):
        """Prints the string representation of an instance based on the class
           name and id. Ex: $ show BaseModel 1234-1234-1234"""
        if not arg:
            print("** class doesn't exist **")
        else:
            args = self.split(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[1]:
                objs = storage.all()
                for k in objs.keys():
                    var = objs[k]
                    if var.id == args[1] and o.__class__.__name__ == args[0]:
                        print(var)
                        break
                else:
                    print("** no instance found **")

    def split(self, arg):
        """separate string read"""
        args = arg.split()
        return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()
