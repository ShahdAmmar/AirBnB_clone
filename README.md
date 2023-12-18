# AirBnB clone

The primary goal of this project is to establish a foundational structure for an Airbnb clone by creating a parent class (BaseModel) that handles instance initialization, serialization, and deserialization. This project will also implement a simple flow for handling data in the form of instances, dictionaries, JSON strings, and files. Furthermore, it involves creating classes for essential components of the Airbnb application, includingUser, State, City, and Place.

## Project Description

### Key tasks
BaseModel Class:

The baseModel class should handle the initialization, serialization, and deserialization of instances.
Establish a seamless flow for serialization and deserialization:
Instance <-> Dictionary <-> JSON String <-> File

Airbnb Classes:

User
State
City
Place
Ensure that these classes inherit from the BaseModel class.

FileStorage engine:

Develop the first storage engin for the project, known as FileStorage
Implement functionality for storing and retrieving instances as files.

Unittests:

Create comprehensive unittests to validate the functionality of all classes and the File Storage engine.
Tests should cover aspects such as instance creation, serialization, deserialization, and storage.

### Console

The HBNBCommand class is created to build the console and it has a prompt of hbnb, the console works interactive and non-interactive modes. The methods created in that class are:

1- quit: which handles exiting the console
2- EOF: It handles the End Of the File
3- emptyline: handles when user enters it + enter shouldn't exceute anything
4- Create: Creates new instance of BaseModel and save it n JSON file
5- Show: prints string representation of instance based on class name and ID
6- Destroy: Deletes an instance based on the class name and id
7- all: Prints all string representation of all instances
8- Update: Updates an instance based on the class name and id

## Command Interpreter Description

The command interpreter manages the project's objects; it can create a new object, retrieve an object from a file, do operations on objects, update attributes of an object, and destroy an object.

### How to start the command interpreter?
str 

### How to use the command interpreter?
write the command and press enter.
if the command is defined, it's excuted
