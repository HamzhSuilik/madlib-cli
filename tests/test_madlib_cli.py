from madlib_cli import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_read_template ():
    with open("./assets/story_2.txt", "r") as file:
        actual =  file.read()
    with open("./assets/expected.txt", "r") as file:
        expected =  file.read()
  
    assert actual == expected