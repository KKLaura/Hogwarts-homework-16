import pytest
from pythoncode.calculator import Calculator

class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("start calculate")
    def teardown_class(self):
        print("end!")

    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(100,300,400)],ids=["int","minus","bigint"])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expect",[(4,2,2),(-1,2,-3),(100,100,0)])
    def test_sub(self,a,b,expect):
        assert  expect == self.calc.sub(a,b)
