""" """

import pathlib

import yamlizer

# import all custom object classes that you want to load and/or dump
from examples.subclass_yamlizable.custom_objects import Employee, Graduate, Student

# paths to the yml configs you want to load/dump custom objects from/to
path_prefix = pathlib.Path.cwd() / "examples/subclass_yamlizable"
load_config_path = path_prefix / "load_config.yml"

# load custom object(s) from load_config.yml
student = yamlizer.load(load_config_path)

# path to the yml config you want to dump custom objects to
dump_config_path = path_prefix / "dump_config.yml"

# instantitate custom objects to dump
employee_one = Employee(salary=2500.50, age=35, name="O", wealth="400000")
employee_two = Employee(salary=5001, age=40, name="T", wealth="$200,000")
graduate = Graduate(
    major="law",
    institution="IUS",
    parents=(employee_one, employee_two),
    age=20,
    name="H",
    wealth="$30,000",
)

# make changes to the custom objects
student.age += 1

# collect the custom objects to be dumped to dump_config.yml in a list
people = [employee_one, employee_two, graduate, student]

# dump custom objects to dump_config.yml
yamlizer.dump(people, dump_config_path)
