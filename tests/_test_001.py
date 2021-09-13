from pathlib import Path
from yamlizer import register, load, dump
from yamlizer import Yamlizable

class TestYamlizable:
    """ """

    def __init__(self, int_, float_, str_, bool_, list_, dict_) -> None:
        self.int_ = int_
        self.float_ = float_
        self.str_ = str_
        self.bool_ = bool_
        self.list_ = list_
        #self.dict_ = dict_

register(TestYamlizable)
configpath = Path.cwd() / "tests/_test_config.yml"

yamlizable = TestYamlizable(
    int_=2,
    float_=1.1,
    str_="test",
    bool_=True,
    list_=[1, 2, 3],
    dict_={"hi": 1, "by": 2},
)
dump(yamlizable, configpath)


"""yamlizable = load(configpath)
print(vars(yamlizable))
"""
