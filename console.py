#!/usr/bin/python3

"""
This is the console module
"""
# -----Note that JSON_file is a list i'm using to test out the code----- #
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class"""
    all_objs = {}
    prompt = "(HBNB) "

    def emptyline(self):
        """Do nothing on emptyline input
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        sys.exit(1)

    def do_EOF(self, line):
        """Exits the console with ctrl+D
        """
        print()
        return True

    def do_create(self, line):
        """Create new instance of BaseModel and prints the id
        """
        if line == "":
            print("** class name is missing **")
        elif line != "BaseModel":
            print("** class does not exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print("{}".format(new_model.id))

    def do_show(self, line):
        """Prints the string representation of an instance based on \
                        the class name and id
        """
        arguments = args(line)
        if input_check(arguments):
            obj = BaseModel(HBNBCommand.all_objs[
                    "{}.{}".format(arguments[0], arguments[1])])
            print(type(obj))
            print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id"""
        arguments = args(line)
        if input_check(arguments):
            del HBNBCommand.all_objs["{}.{}".format(arguments[0], \
                    arguments[1])]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not \
        on the class name"""
        obj_str = []
        for obj in HBNBCommand.all_objs.values():
            obj_str.append(str(obj))
        print(obj_str)

    def update(self, line):
        """
        Updates an instance based on the class and id by adding or \
        updating attribute"""
        print("done update")


def args(arg):
    """
    Convert a line string to an argument tuple"""
    return tuple(arg.split())


def input_check(a_tuple) -> bool:
    if len(a_tuple) > 0:
        if a_tuple[0] == "BaseModel":
            if len(a_tuple) > 1:
                if "{}.{}".format(a_tuple[0], a_tuple[1])\
                        in HBNBCommand.all_objs.keys():
                    return True
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
    else:
        print("** class name missing **")


if __name__ == "__main__":
    storage.reload()
    HBNBCommand.all_objs = storage.all()
    HBNBCommand().cmdloop()
