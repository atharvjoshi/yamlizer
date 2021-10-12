""" """

class Person:
    """ """

    def __init__(self, age: int, name: str, wealth: float) -> None:
        """ """
        self.age = age
        self._name = name
        self._wealth = wealth

    @property
    def name(self) -> str:
        """ """
        return self._name

    @property
    def wealth(self) -> str:
        """ """
        return f"${self._wealth :,.2f}".replace("$-", "-$")

    @wealth.setter
    def wealth(self, value: float) -> None:
        """ """
        self._wealth = value


class Student(Person):
    """ """

    def __init__(self, institution: str, guardians: tuple[Person], **kwargs) -> None:
        """ """
        self.institution = institution
        self.guardians = guardians
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
