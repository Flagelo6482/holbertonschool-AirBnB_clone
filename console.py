#!/usr/bin/python3


"""Console 0.0.1"""


import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "
    file = None
    cls = ["BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg in self.cls:
            new = eval(arg)()
            eval(arg).save(new)
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[1]:
                all_objs = storage.all()
                for key in all_objs.keys():
                    o = all_objs[key]
                    if o.id == args[1] and o.__class__.__name__ == args[0]:
                        print(o)
                        break
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                for key in all_objs.keys():
                    o = all_objs[key]
                    if o.id == args[1] and o.__class__.__name__ == args[0]:
                        del all_objs[key]
                        storage.save()
                        break
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        if not arg:
            all_objs = storage.all()
            lis = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                lis.append(str(obj))
            print(lis)
        elif arg in self.cls:
            all_objs = storage.all()
            lis = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if arg == obj.__class__.__name__:
                    lis.append(str(obj))
            if len(lis) > 0:
                print(lis)
            else:
                print("** class doesn't exist **")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
        adding or updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                all_objs = storage.all()
                for key in all_objs.keys():
                    o = all_objs[key]
                    if o.id == args[1] and o.__class__.__name__ == args[0]:
                        setattr(o, args[2], args[3].strip('"'))
                        break
                else:
                    print("** no instance found **")

    def do_EOF(self, line):
        """When pushing a EOF"""
        return True

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def complete(self, text, state):
        """Return the next possible completion for 'text'.

        If a command has not been entered, then complete against command list.
        Otherwise try to call complete_<command> to get list of completions.
        """
        if state == 0:
            import readline
            origline = readline.get_line_buffer()
            line = origline.lstrip()
            stripped = len(origline) - len(line)
            begidx = readline.get_begidx() - stripped
            endidx = readline.get_endidx() - stripped
            if begidx>0:
                cmd, args, foo = self.parseline(line)
                if cmd == '':
                    compfunc = self.completedefault
                else:
                    try:
                        compfunc = getattr(self, 'complete_' + cmd)
                    except AttributeError:
                        compfunc = self.completedefault
            else:
                compfunc = self.completenames
            self.completion_matches = compfunc(text, line, begidx, endidx)
        try:
            return self.completion_matches[state]
        except IndexError:
            return None

def separarArgs(arg):
    """separamos la linea leida en string separados"""
    argumentos = arg.split()
    return argumentos


if __name__ == '__main__':
    HBNBCommand().cmdloop()
