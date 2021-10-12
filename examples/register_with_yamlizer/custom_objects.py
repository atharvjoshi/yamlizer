""" """

class Person:
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
