import pytest


@pytest.fixture(scope="class")
def setup():
    print("I'll be executing first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("I'm here for passing data to test")
    return ["mahnoor Ismial", "mahnoorismail8@gmail.com"]


@pytest.fixture(params=[("chrome", "maha"), ("firefox", 909), ("IE", "oiu")])
def crossBrowser(request):
   return request.param