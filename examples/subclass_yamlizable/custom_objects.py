""" """

from yamlizer import Yamlizable


class Person(Yamlizable):
    """ """

    def __init__(self, age: int, name: str, wealth: str) -> None:
        """ """
        self.age = age
        self._name = name
        self._wealth = None
        self.wealth = wealth

    @property
    def name(self) -> str:
        """ """
        return self._name

    @property
    def wealth(self) -> str:
        """ """
        return f"${self._wealth :,.2f}".replace("$-", "-$")

    @wealth.setter
    def wealth(self, value: str) -> None:
        """ """
        self._wealth = float(value.replace(",", "").replace("$", ""))


class Student(Person):
    """ """

    def __init__(self, institution: str, parents: list[Person], **kwargs) -> None:
        """ """
        self.institution = institution
        self.parents = parents
        super().__init__(**kwargs)

class Graduate(Student):
    """ """

    def __init__(self, major: str, **kwargs) -> None:
        """ """
        self.major = major
        super().__init__(**kwargs)

class Employee(Person):
    """ """

    def __init__(self, salary: float, **kwargs) -> None:
        """ """
        self.salary = salary
        super().__init__(**kwargs)
