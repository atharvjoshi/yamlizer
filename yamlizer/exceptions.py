""" """

from typing import Any


class YamlMappingError(Exception):
    """ """

    def __init__(self, yamlizable: Any, key: str) -> None:
        """ """
        message = (f"'{key}' must be an attribute of '{yamlizable}'")
        super().__init__(message)
