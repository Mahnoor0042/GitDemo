import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("Executing from fixture Demo")

    def test_fixtureDemo1(self):
        print("Executing from fixture Demo1")

    def test_fixtureDemo2(self):
        print("Executing from fixture Demo2")

    def test_fixtureDemo3(self):
        print("Executing from fixture Demo3")

