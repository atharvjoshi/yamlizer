""" """

from pathlib import Path
from typing import Any, Type

import yaml

from . import yamlmapper


class YamlRegistrar:
    """ """

    def __init__(self) -> None:
        self.register: dict[str, Type] = dict()


_REGISTRAR = YamlRegistrar()


def register(cls: Type[Any]) -> None:
    """ """
    try:
        yaml_tag = cls.__name__
    except AttributeError:
        pass
    else:
        yaml.SafeDumper.add_representer(cls, _represent)
        yaml.SafeLoader.add_constructor(yaml_tag, _construct)
        _REGISTRAR.register[yaml_tag] = cls


def _represent(dumper: yaml.Dumper, yamlizable: Any) -> yaml.MappingNode:
    """ """
    yaml_tag = yamlizable.__class__.__name__
    yaml_map = yamlmapper.yaml_map(yamlizable)
    try:
        return dumper.represent_mapping(yaml_tag, yaml_map)
    except yaml.YAMLError:
        raise


def _construct(loader: yaml.Loader, node: yaml.MappingNode) -> Any:
    """ """
    try:
        kwargs = loader.construct_mapping(node, deep=True)
    except yaml.YAMLError:
        pass
    except TypeError:
        pass
    else:
        cls = _REGISTRAR.register[node.tag]
        return cls(**kwargs)


def dump(config: Any, configpath: Path, mode: str = "w+") -> None:
    """ """
    try:
        with open(configpath, mode=mode) as configfile:
            yaml.safe_dump(config, configfile)
    except IOError:
        raise
    except yaml.YAMLError:
        raise


def load(configpath: Path) -> Any:
    """ """
    try:
        with open(configpath, mode="r") as configfile:
            return yaml.safe_load(configfile)
    except yaml.YAMLError:
        raise
    except IOError:
        raise
