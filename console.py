#!/usr/bin/python3


"""Console 0.0.1"""


import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = '(hbnb) '
    cls = ["BaseModel"]
    file = None

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
        elif arg in self.cls:
            new = eval(arg)()
            eval(arg).save(new)
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Comentario"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
        else:
            args = splt_args(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[1]:
                all_objs = storage.all()
                for k in all_objs.keys():
                    var = all_objs[key]
                    if var.id == args[1] and var.__class__.__name__ == args[0]:
                        print(var)
                        break
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Comentario"""
        if not arg:
            print("** class name missing **")
        else:
            args = splt_args(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                for key in all_objs.keys():
                    var = all_objs[key]
                    if var.id == args[1] and var.__class__.__name__ == args[0]:
                        del all_objs[key]
                        storage.save()
                        break
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Comentario"""
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

    def complete(self, text, state):
        """Comentario"""
        if state == 0:
            import readline
            line_or = readline.get_line_buffer()
            line = origline.lstrip()
            ppd = len(line_or) - len(line)
            g_dx = readline.get_begidx() - stripped
            d_dx = readline.get_endidx() - stripped

            if g_dx > 0:
                cdm, args, foo = self.parseline(line)
                if cmd == '':
                    func = self.completedefault
                else:
                    try:
                        func = getattr(self, 'complete_' + cmd)
                    except AttributeError:
                        func = self.completedefault
            else:
                func = self.completenames
            self.completion_matches = func(text, line, g_dx, d_dx)
        try:
            return self.completion_matches[state]
        except IndexError:
            return None

    def do_update(self, arg):
        """Comentario"""
        if not arg:
            print("** class name missing **")
        else:
            args = splt_args(arg)
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
                for k in all_objs.keys():
                    var = all_objs[k]
                    if var.id == args[1] and var.__class__.__name__ == args[0]:
                        setattr(var, args[2], args[3].strip('"'))
                        break
                else:
                    print("** no instance found **")

    def splt_args(arg):
        """Comentario"""
        arg = arg.split()
        return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()
