def is_palindrome(s):
    r=s[::-1]
    if r==s:
        print("The string is palindrome")
    else:
        print("Not a palindrome")
is_palindrome("madam")