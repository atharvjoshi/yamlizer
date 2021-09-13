""" """

from typing import Any

class YamlMappingError(Exception):
    """ """

    def __init__(self, yamlizable: Any, key: str) -> None:
        """ """
        message = (f"Please make '{key}' an attribute of '{yamlizable}'")
        super().__init__(message)
