from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hi" == more_hello()


def test_more_hello_2():
    assert "bi" == more_goodbye()