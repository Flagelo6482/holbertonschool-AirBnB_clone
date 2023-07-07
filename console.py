#!/usr/bin/python3


"""Console 0.0.1"""


import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
