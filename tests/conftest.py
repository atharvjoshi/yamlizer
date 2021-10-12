""" """

import pytest

from yamlizer import Yamlizable


class Data(Yamlizable):
    """ """

    def __init__(
        self,
        data: dict = {
            "set": {None, True},
            "list": [0, 1.0, 2e2, 1, b"a", "f"],
        },
    ) -> None:
        """ """
        self.data = data

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.data == other.data
        return False


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
def data() -> Data:
    """ """
    return Data()


@pytest.fixture
def data_yaml_map() -> dict:
    """ """
    return {
        "data": {
            "list": [0, 1.0, 2e2, 1, b"a", "f"],
            "set": {None, True},
        }
    }


@pytest.fixture
def datachild() -> DataChild:
    """ """
    return DataChild()


@pytest.fixture
def datachild_yaml_map() -> dict:
    """ """
    return {
        "data": {
            "list": [0, 1.0, 2e2, 1, b"a", "f"],
            "set": {None, True},
        },
        "level": 1,
    }


@pytest.fixture
def datagrandchild() -> DataGrandChild:
    """ """
    return DataGrandChild()


@pytest.fixture
def datagrandchild_yaml_map() -> dict:
    """ """
    return {
        "data": {
            "list": [0, 1.0, 2e2, 1, b"a", "f"],
            "set": {None, True},
        },
        "level": 1,
        "name": "X",
    }


@pytest.fixture
def info() -> Info:
    """ """
    return Info()


@pytest.fixture
def info_yaml_map() -> Info:
    """ """
    return {
        "info": Data(),
    }
