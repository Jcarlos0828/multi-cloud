def is_palindrome(s1: str) -> bool:
    return s1 == s1[::-1]
print(is_palindrome('radasr'))