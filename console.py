#!/usr/bin/python3
"""This is the console module
"""

import cmd, sys


class HBNBCommand(cmd.Cmd):
    """The console class"""

    prompt = "(HBNB)"

    def emptyline(self):
        """Do nothing on emptyline input"""
        pass

    def do_quit(self, arg):
        """Exit from the interpreter"""
        sys.exit(1)

    def do_EOF(self, arg):
        """Exits the console with ctrl+D"""
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
