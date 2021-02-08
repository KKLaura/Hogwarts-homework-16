import pytest

def add_funcrion(a,b):
    return a+b


@pytest.mark.parametrize("a",[0,1])
@pytest.mark.parametrize("b",[2,3])
def test_add(a,b):
    print("测试数据组合： a->%s,b->%s"%(a,b))

