""" """

import pytest

from yamlizer import Yamlizable


class Data(Yamlizable):
    """ """

    def __init__(
        self,
        data: dict = {
            "set": {None, True},
            "tuple": (b"a", "f"),
            "list": [0, 1.0, 2e2, 1 + 2j],
        },
    ) -> None:
        """ """
        self.data = data


class DataChild(Data):
    """ """

    def __init__(self, *, level: int = 1, **kwargs) -> None:
        """ """
        self.level = level
        super().__init__(**kwargs)


class DataGrandChild(DataChild):
    """ """

    def __init__(self, name: str = "X", **kwargs) -> None:
        """ """
        self.name = name
        super().__init__(**kwargs)


class Info:
    """ """

    def __init__(
        self,
        info: Data = Data(),
    ) -> None:
        """ """
        self.info = info

@pytest.fixture
def get_data() -> Data:
    """ """
    return Data()

@pytest.fixture
def get_data_child() -> DataChild:
    """ """
    return DataChild()

@pytest.fixture
def get_data_grandchild() -> DataGrandChild:
    """ """
    return DataGrandChild()

@pytest.fixture
def get_info() -> Info:
    """ """
    return Info()
