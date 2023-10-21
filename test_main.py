from main import is_palindrome


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 'radar'


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


### Run to see failed test
# def test_hello_add():
#     assert add(test_hello_add.x) == 12

def test_main_isPalindrome():
    assert is_palindrome(test_main_isPalindrome.x) == True