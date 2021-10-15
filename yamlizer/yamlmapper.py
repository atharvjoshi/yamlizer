# -*- coding: utf-8 -*-
"""This module contains utilities to generate yaml maps.

The yaml map is a dictionary that maps the names of keyword arguments required to
initialize a custom object ("Yamlizable") to the values of the yamlizable's attributes
with the same name. Yaml maps are stored in a yaml configuration file under the
yamlizable's custom yaml tag. Yamlizer reads yaml maps from configuration files and
instantiates objects with a `Yamlizable(**yaml_map)` call."""

import inspect
from typing import Any


class YamlMappingError(Exception):
    """Raised if the name of a keyword argument passed to an object's `__init__()` is
    not an attribute of its instance."""


def yaml_map(yamlizable: Any) -> dict[str, Any]:
    """Generates the yaml map of the given yamlizable.

    Args:
        yamlizable (Any): instance to be yaml mapped.

    Raises:
        YamlMappingError: if the name of a keyword argument in the yamlizable's
        __init__() is not its attribute.

    Returns:
        dict[str, Any]: map of the names of keyword arguments in yamlizable's __init__()
        method and the values of yamlizable's attributes with that name."""
    # traverse the yamlizable's MRO to find names of arguments passed to __init__()
    mro = inspect.getmro(type(yamlizable))
    yaml_map_keys = set()
    for class_ in mro:
        # assume that any **kwargs are passed up the MRO to instantiate ancestors
        found_kwargs = False  # if true, visit parent class' __init__()
        init_params = inspect.signature(class_.__init__).parameters.values()

        for param in init_params:
            # add bound keyword arguments (except "self") to yaml_map_keys
            is_param_unbound = param.kind in (param.VAR_KEYWORD, param.VAR_POSITIONAL)
            is_yaml_map_key = not param.name == "self" and not is_param_unbound
            if is_yaml_map_key:
                yaml_map_keys.add(param.name)
            if param.kind == param.VAR_KEYWORD:
                found_kwargs = True
        if not found_kwargs:
            break

    yaml_map_ = {}
    for key in yaml_map_keys:
        if not hasattr(yamlizable, key):
            raise YamlMappingError(f"'{key}' must be an attribute of '{yamlizable}'")
        else:
            value = getattr(yamlizable, key)
            yaml_map_[key] = value
    return yaml_map_
