#!/usr/bin/python3


"""Console 0.0.1"""


import cmd
from models.base_model import BaseModel
from models import storage

class_home = {
    "BaseModel": BaseModel
}


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """By entering quit, we exit the loop"""
        return True

    def do_EOF(self, arg):
        """Clean way out"""
        return True

    def emptyline(self):
        pass

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_create(self, arg):
        """Comentario"""
        if not arg:
            print("** class name missing **")
            return
        clases = {"BaseModel": BaseModel}
        class_name = arg.split()[0]

        if class_name not in clases:
            print("** class doesn't exist **")
            return
        new_instance = clases[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Comentario"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in class_home:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            v_str = f"{args[0]}.{args[1]}"
            if v_str not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[v_str])

    def do_destroy(self, arg):
        """Comentario"""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in class_home:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            v_str = f"{args[0]}.{args[1]}"
            if v_str not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(v_str)
                storage.save()

    def do__all(self, arg):
        """Comentario"""
        lis = []

        if arg == "":
            print([str[v] for k, v in storage.all().items()])
        else:
            args = arg.split(" ")
            if args[0] not in class_home:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    cls = k.split(".")
                    if cls[0] == args[0]:
                        lis.append(str(v))
                print(lis)

    def do_update(self, arg):
        """Comentario"""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in class_home:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            v_str = f"{args[0]}.{args[1]}"
            if v_str not in storage.all().keys():
                print("** no instance found **")
                return
            elif len(args) < 3:
                print("** atribute name missing **")
                return
            elif len(args) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[v_str], args[2], args[3])
                storage.save()

    def do_count(self, arg):
        """Comentario"""
        cls = globals().get(arg, None)
        if cls is None:
            print("** class doesn't exist **")
            return
        count = 0
        for x in storage.all().values():
            if x.__class__.__name__ == arg:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
