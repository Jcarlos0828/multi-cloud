def is_palindrome(s1: str) -> bool:
    s1 = ''.join(s1.split(' '))
    print(s1)
    return s1 == s1[::-1]

def has_space(s1: str) -> bool:
    if s1.find(' ') != -1:
        return False
    return True
print(is_palindrome('anita lava la tina'))
