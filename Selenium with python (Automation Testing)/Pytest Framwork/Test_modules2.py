import pytest

class Test_function:
    @pytest.fixture() # docorator
    def steup(self):
        print("Lunching the browser")
        print("Opem application")
        yield
        print("closing browser")

    def test_login(self):
        print("Test_login")
    def test_search(self):
        print("Test_search")
    def test_Adancedsearch(self):
        print("Test_Adancedsearch")

