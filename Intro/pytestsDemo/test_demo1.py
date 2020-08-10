# any pytest file name must start with 'test_' or end with '_test'
# pytest method names should start with 'test'
# all code must be wrapped into the methods/function
# -k stands for method name execution, -s logs in output, -v stands for more info into metadata
# you may run specific file with test.py <filename.py>
# you can skip test with @pytest.mark.skip
# pytest.mark.xfail
# fixtures are used as setup and teardown methods for test cases, conftest file to generalize
# fixtures and make it available to all test cases (set fixture name as parameters of methods to call it)
# datadriven anad parameterization (send data to test cases via fixtures) can be done with return statements
# in tuple format
# with parameterization you can run a test multiple times with different situations
# when you define fixture scope to class only, it will run once before class is initiated and at the end after
# all the class methods are executed
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("hello")

def test_checkCreditcard(setup):
    msg = "Good Morning Pakistan"
    print(msg)

def test_crossBrowser(crossBrowser):
    print(crossBrowser)