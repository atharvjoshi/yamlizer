""" """

import pathlib

import pytest

import yamlizer

def test_register(info):
    """ """
    class_ = info.__class__
    yamlizer.register(class_)
    assert yamlizer.yamlizer._REGISTRAR.register["Info"] == class_


@pytest.mark.parametrize("test_input", [1, "A", {"a": 1, "b": 2}, [1.0, 2.0, 3.0]])
def test_register_bad_input(test_input):
    """ """
    with pytest.raises(yamlizer.YamlRegistrationError):
        yamlizer.register(test_input)


def test_dump_load(data, datachild, datagrandchild):
    """ """
    configpath = pathlib.Path.cwd() / "tests/test_config.yml"
    config = [data, datachild, datagrandchild]
    yamlizer.dump(config, configpath, mode="w+")
    config = yamlizer.load(configpath)
    assert config == [data, datachild, datagrandchild]
    