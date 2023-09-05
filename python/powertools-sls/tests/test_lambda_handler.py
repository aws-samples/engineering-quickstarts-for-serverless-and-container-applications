from src.handler import hello, hello_name


def test_hello():
    assert hello() == {"message": "hello unknown!"}


def test_hello_name():
    assert hello_name("Sherlock") == {"message": f"hello Sherlock!"}
