#!/usr/bin/python3

"""
This is the console module
"""
import cmd
from models import base_model, user, state, place, city, amenity, review
from models import storage


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class"""
    all_objs = {}
    prompt = "(HBNB) "
    classes = {
            "BaseModel": base_model.BaseModel,
            "User": user.User,
            "State": state.State,
            "Place": place.Place,
            "City": city.City,
            "Amenity": amenity.Amenity,
            "Review": review.Review
            }
    err_msg = [
                    "** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    "** attribute name missing **",
                    "** value missing **"
                    ]

    def __check_attr(self, arg):
        if not self.__check_id(arg):
            return False
        if len(arg) > 2:
            if len(arg) > 3:
                return True
            else:
                print(HBNBCommand.err_msg[5])
                return False
        else:
            print(HBNBCommand.err_msg[4])
            return False

    def __check_class(self, arg):
        if len(arg) > 0:
            if arg[0] in HBNBCommand.classes:
                return True
            else:
                print(HBNBCommand.err_msg[1])
                return False
        else:
            print(HBNBCommand.err_msg[0])
            return False

    def __check_id(self, arg):
        if not self.__check_class(arg):
            return False
        if len(arg) > 1:
            if "{}.{}".format(arg[0], arg[1]) \
                    in HBNBCommand.all_objs.keys():
                return True
            else:
                print(HBNBCommand.err_msg[2])
                return False
        else:
            print(HBNBCommand.err_msg[3])
            return False

    def emptyline(self):
        """Do nothing on emptyline input
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exits the console with ctrl+D
        """
        print()
        return True

    def do_create(self, line):
        """Create new instance of BaseModel and prints the id
        """
        if not line:
            print("** class name is missing **")
        elif line not in HBNBCommand.classes:
            print("** class does not exist **")
        else:
            for cls_name in HBNBCommand.classes:
                if cls_name == line:
                    new_model = HBNBCommand.classes[cls_name]()
            new_model.save()
            print("{}".format(new_model.id))

    def do_show(self, line):
        """Prints the string representation of an instance based on \
                        the class name and id
        """
        arguments = args(line)
        if self.__check_id(arguments):
            obj = HBNBCommand.all_objs[
                    "{}.{}".format(arguments[0], arguments[1])]
            # print(type(obj))
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arguments = args(line)
        if self.__check_id(arguments):
            del HBNBCommand.all_objs["{}.{}".format(
                arguments[0], arguments[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not \
        on the class name"""
        arguments = args(line)
        obj_str = []
        for obj in HBNBCommand.all_objs.values():
            obj_str.append(str(obj))
        if arguments:
            if not self.__check_class(arguments):
                return
            else:
                obj_str = []
                for key, obj in HBNBCommand.all_objs.items():
                    if arguments[0] == key.split(".")[0]:
                        obj_str.append(str(obj))
                print(obj_str)
        else:
            print(obj_str)

    def __parse_type(self, arg):
        try:
            arg = float(arg)
            try:
                arg = int(arg)
                return arg
            except Exception:
                return float(arg)
        except Exception:
            return str(arg)

    def do_update(self, line):
        """
        Updates an instance based on the class and id by adding or \
        updating attribute"""
        # TODO:
        # 1 all_obj dict already contains objects...
        # ...with index <class name>.<id>
        # 2 convert object to dict using object.to_dict()
        # 3 update <attribute name> of object with <attribute value>
        # 4 update object at index <class name>.<id> in all_objs dict
        # 5 call storage.save() to save changes to json file
        arguments = args(line)
        if not self.__check_attr(arguments):
            return
        obj = HBNBCommand.all_objs[
                "{}.{}".format(arguments[0], arguments[1])]
        val = arguments[3].strip('"')
        val = self.__parse_type(val)
        obj.attr_update({arguments[2]: val})

        # Basically: object -> dict -> object -> save_object


def args(arg):
    """
    Convert a line string to an argument tuple"""
    return tuple(arg.split())


if __name__ == "__main__":
    storage.reload()
    HBNBCommand.all_objs = storage.all()
    HBNBCommand().cmdloop()
