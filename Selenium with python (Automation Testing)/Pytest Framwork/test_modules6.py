import pytest

class testClass:
    @pytest.mark.parametrize("num1, num2",[(1,1), (3,5),(5,20),(6,39)])
    def test1(self, num1, num2):
        assert num1 == num2
