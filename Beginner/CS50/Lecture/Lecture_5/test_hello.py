from hello import hello

def test_hello():
    assert hello("David") == "hello, David"
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"
