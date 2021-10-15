# -*- coding: utf-8 -*-
"""This module contains utilities that allow custom object classes to register with
yamlizer by inheriting from `Yamlizable`."""

import yaml

from . import yamlmapper
from .yamlizer import YamlizationError


class YamlizableMetaclass(type):
    """Metaclass for `Yamlizable`.

    Inspired by PyYAML's `YAMLObjectMetaclass`, this metaclass marks its descendents as
    safe for loading (dumping) by giving them a yaml_tag and registering them with
    PyYAML's `SafeLoader` and `SafeDumper`."""

    def __init__(cls, name, bases, kwds) -> None:
        super().__init__(name, bases, kwds)
        cls._yaml_tag = name
        cls._yaml_dumper = yaml.SafeDumper
        cls._yaml_dumper.add_representer(cls, cls._to_yaml)
        cls._yaml_loader = yaml.SafeLoader
        cls._yaml_loader.add_constructor(cls._yaml_tag, cls._from_yaml)

    def __repr__(cls) -> str:
        return f"<class '{cls.__name__}>"


class Yamlizable(metaclass=YamlizableMetaclass):
    """A class that allows its descendents to be loaded from (dumped to) yaml files.

    Args:
        metaclass ([type], optional): Metaclass that handles registration with PyYAML.
        Defaults to YamlizableMetaclass.
    """

    def __repr__(self) -> str:
        """A convenient string representation that contains the current yaml map of this
        yamlizable 

        Returns:
            str: the string representation of this yamlizable
        """
        yaml_map = yamlmapper.yaml_map(self)
        yaml_map_items = [f"{k}={v!r}" for k, v in sorted(yaml_map.items())]
        return f"{self.__class__.__name__}({', '.join(yaml_map_items)})"

    @classmethod
    def _to_yaml(cls, dumper: yaml.SafeDumper, yamlizable) -> yaml.MappingNode:
        """Representer for Yamlizables

        Args:
            dumper (yaml.SafeDumper): PyYAML's `SafeDumper`.
            yamlizable (Any): A yamlizable instance to be dumped to yaml.

        Returns:
            yaml.MappingNode: Yaml map representation of the given yamlizable
        """
        yaml_map = yamlmapper.yaml_map(yamlizable)
        return dumper.represent_mapping(yamlizable._yaml_tag, yaml_map)

    @classmethod
    def _from_yaml(cls, loader: yaml.SafeLoader, node: yaml.MappingNode):
        """Constructor for Yamlizables

        Args:
            loader (yaml.SafeLoader): PyYAML's `SafeLoader`.
            node (yaml.MappingNode): Yaml map for initializing an instance of a
            Yamlizable

        Raises:
            YamlizationError: If the yamlizable cannot be instantiated with the loaded
            yaml map.

        Returns:
            [type]: Initialized yamlizable instance
        """
        try:
            kwargs = loader.construct_mapping(node, deep=True)
            return cls(**kwargs)
        except TypeError:
            raise YamlizationError(f"Yaml map incompatible with {cls} init()") from None
