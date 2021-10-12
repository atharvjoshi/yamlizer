""" """

import pathlib

import yamlizer

# import custom object classes to register and then load and/or dump
from examples.register_with_yamlizer.custom_objects import Person

# path to the yml config you want to load/dump custom objects from/to
configpath = pathlib.Path.cwd() / "examples/register_with_yamlizer/config.yml"

# register custom object class with yamlizer
yamlizer.register(Person)

# instantiate custom object
person = Person(age=10, name="B", wealth="0.00")

# dump custom object to config.yml
yamlizer.dump(person, configpath)

# load same object from config.yml
person = yamlizer.load(configpath)

# view object attributes
print(f"{person.age = }, {person.name = }, {person.wealth = } ")
