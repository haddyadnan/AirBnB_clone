#!/usr/bin/python3
"""This is the console module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The console class"""

    prompt = "(HBNB) "

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

    def do_create(self, *args):
        """Create new instance of BaseModel and prints the id"""
        print("done create")

    def do_show(self, *args):
        """Prints the string representation of an instance based
        the class name and id
        """
        print("done show")

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id
        """
        print("done destroy")

    def all(self, *args):
        """Prints all string representation of all instances based or not
        on the class name
        """
        print("done all")

    def update(self, *args):
        """Updates an instance based on the class and id by adding or
        updating attribute
        """
        print("done update")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
