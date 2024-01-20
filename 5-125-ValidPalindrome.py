

def isPalindrome(s):
    if len(s) < 2:
        return True

    s1 = ""
    for char in s:
        if char.isalnum():
            s1 += char.lower()

    return s1 == s1[::-1]


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))

