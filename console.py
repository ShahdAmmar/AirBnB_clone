#!/usr/bin/python3
""" console command intrepreter """

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sys


class HBNBCommand(cmd.Cmd):
    """Creating the HNBN cmd"""

    prompt = "(hbnb) " if sys.__stdin__.isatty() else ''
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }


    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_quit(self, args):
        """ The quit method to quite the cmd"""
        return True

    def help_quit(self):
        """ Method used to provide help documentations from the cmd for quit command """
        print("Quit command to exit the program")

    def do_EOF(self, args):
        """ The EOF (End-Of-File) method to exit the program """
        return True

    def help_EOF(self):
        """ Method used to provide help documentations from the cmd for EOF command """
        print("EOF command to exit the program")

    def empty_line(self):
        """Empty line method which handles when user enters it + enter shouldn't exceute anything"""
        pass

    def do_create(self, args):
        """ Creates new instance of BaseModel and save it n JSON file"""
        splitted_command = shlex.split(args)
        if not splitted_command: #checks if there is a class name entered or not using len
            print("** class name missing **")
            return

        elif splitted_command[0] not in self.__classes: # checks if the first argument not in the valid classes
            print("** class doesn't exist **")
        else:
            new_ins = eval(splitted_command[0] + '()')
            new_ins.save()
            print(new_ins.id) #print the ID of the created instance

    def do_show(self, args):
        """Method that prints the string representation of an instance based on class name and ID"""
        splitted_command = shlex.split(args)
        if len(splitted_command) == 0:
            print("** class name missing **")
        elif splitted_command[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(splitted_command) < 2: #checks if the splitted command is less than two tokens
            print("** instance id missing **") #Means that only the class name was provided and ID not provided
        else:
            all_objects = storage.all() #fetch all the objects from storage
            key = splitted_command[0] + "." + splitted_command[1]
            if key in all_objects: #checks if the key is in objects
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        splitted_command = shlex.split(args)
        if len(splitted_command) == 0:
            print("** class name missing **")
        elif splitted_command[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(splitted_command) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = splitted_command[0] + "." + splitted_command[1]
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances """
        llist = []
        all_objects = storage.all()
        splitted_command = shlex.split(args)
        if len(splitted_command) == 0:
            for key, value in all_objects.items():
                llist.append(str(value))
        elif splitted_command[0] not in self.__classes:
                print("** class doesn't exist **")
                return
        else:
            for key, value in all_objects.items():
                if key.split('.')[0] == splitted_command[0]:
                    llist.append(str(value))
        print(llist)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        splitted_command = shlex.split(args)
        if len(splitted_command) == 0:
            print("** class name missing **")
        elif splitted_command[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(splitted_command) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = splitted_command[0] + "." + splitted_command[1]
            if key not in all_objects:
                print("** no instance found **")
            elif len(splitted_command) < 3:
                print("** attribute name missing **")
            elif len(splitted_command) < 4:
                print("** value missing **")
            else:
                updated_obj = all_objects[key]

                attribute_name = splitted_command[2]
                attribute_value = splitted_command[3]

                try:
                    attribute_value = eval(attribute_value)
                except Exception:
                    pass
                setattr(updated_obj, attribute_name, attribute_value)

                updated_obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
