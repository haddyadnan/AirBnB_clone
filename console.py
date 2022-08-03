#!/usr/bin/python3

"""
This is the console module
"""
# -----Note that JSON_file is a list i'm using to test out the code----- #
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class"""
    prompt = "(HBNB) "

    def emptyline(self):
        """Do nothing on emptyline input"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        sys.exit(1)

    def do_EOF(self, line):
        """Exits the console with ctrl+D"""
        print()
        return True

    def do_create(self, line):
        """Create new instance of BaseModel and prints the id"""
        if line == "":
            print("** class name is missing **")
        elif line != "BaseModel":
            print("** class does not exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print("{}".format(new_model.id))

    def do_show(self, line):
        """Prints the string representation of an instance based \
        the class name and id"""
        arguments = args(line)
        if len(arguments) > 0:
            if arguments[0] == "BaseModel":
                if len(arguments) > 1:
                    if arguments[1] in HBNBCommand.__JSON_file:
                        print("done show")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        print("done destroy")

    def all(self, line):
        """Prints all string representation of all instances based or not \
        on the class name"""
        print("done all")

    def update(self, line):
        """Updates an instance based on the class and id by adding or \
        updating attribute"""
        print("done update")


def args(arg):
    """Convert a line string to an argument tuple"""
    return tuple(arg.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
