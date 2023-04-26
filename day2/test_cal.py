import pytest
from add import add

def teardown_module():
    print("【结束测试】")

def setup_function():
    print("\n【开始计算】")

def teardown_function():
    print("\n【结束计算】")


@pytest.mark.parametrize(
    "num1,num2,expect",
    [
        ["a", 20, "a参数为非数字"],
        [67, "m", "b参数为非数字"],
        [670, 10, "a参数大小超出范围"],
        [49, 100, "b参数大小超出范围"],
        [30, 40, 70]
    ]
)
def test_caladd(num1, num2, expect):
    """
    测试用例，被测函数为add.py文件中的add函数
    用例1：输出为“a参数为非数字”
    用例2：输出为“b参数为非数字”
    用例3：输出为“a参数大小超出范围”
    用例4：输出为“b参数大小超出范围”
    用例5：输出两个参数的和
    :return:
    """
    # 调用被测函数
    result = add(num1, num2)
    # 断言
    assert result == expect