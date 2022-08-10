#!/usr/bin/python3

"""
This is the console module
"""
import cmd
from models import base_model, user, state, place, city, amenity, review
from models import storage
import re


methods = [
    "update",
    "all",
    "destroy",
    "show",
]


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class"""

    all_objs = {}
    prompt = "(hbnb) "  # space after bracket to note result
    classes = {
        "BaseModel": base_model.BaseModel,
        "User": user.User,
        "State": state.State,
        "Place": place.Place,
        "City": city.City,
        "Amenity": amenity.Amenity,
        "Review": review.Review,
    }
    """
    dictionary of all classes
    """
    err_msg = [
        "** class name missing **",
        "** class doesn't exist **",
        "** no instance found **",
        "** instance id missing **",
        "** attribute name missing **",
        "** value missing **",
    ]
    """list of all error messages
    """

    def __check_attr(self, arg):
        """Private: checks for attribute"""
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
        """Private: checks for class"""
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
        """Private: checks for id"""
        self.__reload()
        if not self.__check_class(arg):
            return False
        if len(arg) > 1:
            if "{}.{}".format(arg[0], arg[1]) in HBNBCommand.all_objs.keys():
                # print(f"second: {arg[0]}.{arg[1]}")
                return True
            else:
                print(HBNBCommand.err_msg[2])
                return False
        else:
            print(HBNBCommand.err_msg[3])
            return False

    def __reload(self):
        """Private: reloads all objects from storage to all_objs dict"""
        storage.reload()
        HBNBCommand.all_objs = storage.all()

    def emptyline(self):
        """Do nothing on emptyline input"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the console with ctrl+D"""
        print()
        return True

    def do_create(self, line):
        """Create new instance of BaseModel and prints the id"""
        line = line.strip()
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for cls_name in HBNBCommand.classes:
                if cls_name == line:
                    new_model = HBNBCommand.classes[cls_name]()
            new_model.save()
            print("{}".format(new_model.id))

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id
        """
        self.__reload()
        arguments = self.args(line)
        # print("here: ", arguments[0], arguments[1])
        if self.__check_id(arguments):
            # replace .format with f-string to meet pycodestyle
            obj = HBNBCommand.all_objs[f"{arguments[0]}.{arguments[1]}"]
            # .format(arguments[0], arguments[1])]
            # print(type(obj))
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        self.__reload()
        arguments = self.args(line)
        if self.__check_id(arguments):
            # replace .format with f-string pycodestyle
            del HBNBCommand.all_objs[f"{arguments[0]}.{arguments[1]}"]  #
            # .format(arguments[0], arguments[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name
        """
        self.__reload()
        arguments = self.args(line)
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
        """casts update value to appropriate type"""
        try:
            arg = float(arg)
            if arg - int(arg) > 0:
                return float(arg)
            else:
                return int(arg)
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
        self.__reload()
        arguments = self.args(line)
        # print("here: ", arguments[0], arguments[1],
        #  arguments[2], arguments[3])
        if not self.__check_attr(arguments):
            return
        obj = HBNBCommand.all_objs["{}.{}".format(arguments[0], arguments[1])]
        val = arguments[3].strip('"')
        val = self.__parse_type(val)
        obj.attr_update({arguments[2]: val})

        # Basically: object -> dict -> object -> save_object

    def __parse_cmd(self, command, arg):
        cmds = {
            ".create": self.do_create,
            ".show": self.do_show,
            ".all": self.do_all,
            ".destroy": self.do_destroy,
            ".update": self.do_update,
            ".count": self.do_count,
        }
        if "(" and ")" in arg:
            arg_list = arg.split("(")
            # arg_list = arg_list.strip(",")
            # arg_list = arg_list.strip('"')
        else:
            return
        new_arg = arg_list[1][:-1].split()
        new_arg = new_arg.strip(',')
        new_arg = new_arg.replace('"', '')
        new_arg = "{} {}".format(command, new_arg)
        for k, func in cmds.items():
            if k == arg_list[0]:
                func(new_arg)

    def do_BaseModel(self, arg):
        """Usage: BaseModel.<command>"""
        self.__parse_cmd("BaseModel", arg)

    def do_User(self, arg):
        """Usage: User.<command>"""
        self.__parse_cmd("User", arg)

    def do_City(self, arg):
        """Usage: City.<command>"""
        self.__parse_cmd("City", arg)

    def do_State(self, arg):
        """Usage: State.<command>"""
        self.__parse_cmd("State", arg)

    def do_Amenity(self, arg):
        """Usage: Amenity.<command>"""
        self.__parse_cmd("Amenity", arg)

    def do_Place(self, arg):
        """Usage: Place.<command>"""
        self.__parse_cmd("Place", arg)

    def do_Review(self, arg):
        """Usage: Review.<command>"""
        self.__parse_cmd("Review", arg)

    def args(self, arg):
        """Convert a line string to an argument tuplei"""
        return tuple(arg.split())

    def do_count(self, class_name):
        self.__reload()  # storage.reload wont work unless all is called
        obj_count = 0
        for obj_key in HBNBCommand.all_objs.keys():
            if class_name.strip(" ") == obj_key.split(".")[0]:
                obj_count = obj_count + 1
        print(obj_count)

        #########################################
        # ##########Checking Default##############
        #########################################

        # def default(self, line):
        """
        print line
        """
        """
        # tmp = re.search(r"(^[^.]*)", line).group(0)
        if line.split(".")[0] in self.classes.keys():

            obj = line.split(".")[0]
            # self.do_all(dc)

            # obj = line.split(".")[0]
            methd = re.search(r"(?<=\.)(.*?)(?=\()", line).group(0)
            if methd in methods:
                val = re.search(r"(?<=\()(.*?)(?=\))", line).group(0)
                # args = "do_" + str(args)
                # print(args)
                methd = "do_" + methd

                if any(val):
                    val = re.sub('"', "", val)
                    eval(f"self.{methd}")(f"{obj} {val}")
                else:
                    eval(f"self.{methd}(obj)")
        else:
            print(f"*** Unknown syntax: {line}")
            """


if __name__ == "__main__":
    """
    main loop
    """
    HBNBCommand().cmdloop()
