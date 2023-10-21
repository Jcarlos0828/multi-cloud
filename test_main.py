from main import is_palindrome, has_space


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 'radar'
    function.y = 'anita lava la tina'


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x
    del function.y


### Run to see failed test
# def test_hello_add():
#     assert add(test_hello_add.x) == 12

def test_main_isPalindrome():
    assert is_palindrome(test_main_isPalindrome.x) == True
    assert is_palindrome(test_main_isPalindrome.y) == True


def test_main_hasSpace():
    assert has_space(test_main_hasSpace.x) == True
    assert has_space(test_main_hasSpace.y) == False

