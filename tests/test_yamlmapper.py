""" """

import pytest

from yamlizer import yamlmapper


def test_yaml_map(
    info,
    data,
    datachild,
    datagrandchild,
    info_yaml_map,
    data_yaml_map,
    datachild_yaml_map,
    datagrandchild_yaml_map,
):
    """ """
    assert yamlmapper.yaml_map(info) == info_yaml_map
    assert yamlmapper.yaml_map(data) == data_yaml_map
    assert yamlmapper.yaml_map(datachild) == datachild_yaml_map
    assert yamlmapper.yaml_map(datagrandchild) == datagrandchild_yaml_map
