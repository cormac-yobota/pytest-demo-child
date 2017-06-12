pytest_plugins = "tests.conftest"

def test_fixture_says_hello(hello):
    assert hello == "hello!!"

