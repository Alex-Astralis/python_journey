def is_palindrome_clean_string_version(s: str) -> bool:
    """
    Return True if the string `s` is a palindrome after
    removing non-alphanumeric characters and ignoring case.

    Args:
        s (str): Input string

    Returns:
        bool: True if palindrome, else False
    """

    if not s:
        return True

    clean_string = ''.join( char.lower() for char in s if char.isalnum() )

    for i in range(len(clean_string) // 2):
        if clean_string[i] != clean_string[-(i+1)]:
            return False

    return True

def is_palindrome_two_pointer_version(s: str) -> bool:
    """
    Return True if the string `s` is a palindrome after
    removing non-alphanumeric characters and ignoring case.

    Args:
        s (str): Input string

    Returns:
        bool: True if palindrome, else False
    """

    if not s:
        return True

    a, b = 0, (len(s) - 1)

    while a < b:
        while a < b and not s[a].isalnum():
            a += 1
        while a < b and not s[b].isalnum():
            b -= 1

        if s[a].lower() != s[b].lower():
            return False

        a += 1
        b -= 1

    return True

# Defaulting to Two-Pointer version, as o(1) space efficient.
is_palindrome = is_palindrome_clean_string_version
