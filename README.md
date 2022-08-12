# AirBnB Clone - Console
## Description of the project
This is the first step towards building a full web application: the AirBnB clone. The airbnb console is a shell like terminal used to manage the airbnb project objects. The console is used to:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### How to start the project
To start the project, run the console.py file

`
./console.py
`

### Examples
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help     show

Undocumented commands:
======================
count

(hbnb) help User
Usage: User.<command>
(hbnb) help create
Create new instance of model and prints the id
(hbnb) create User
1f700744-f2cb-48c8-8836-31cad99e125f
(hbnb) User.all()
["[User] (1f700744-f2cb-48c8-8836-31cad99e125f) {'id': '1f700744-f2cb-48c8-8836-31cad99e125f', 'created_at': datetime.datetime(2022, 8, 9, 11, 37, 7, 346575), 'updated_at': datetime.datetime(2022, 8, 9, 11, 37, 7, 346621)}"]
(hbnb) quit()
$
```
