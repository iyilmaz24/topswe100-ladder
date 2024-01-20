

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """

    ptr2 = len(s) - 1
    for i in range(0, len(s)//2):
        s[i], s[ptr2] = s[ptr2], s[i]
        ptr2 -= 1


s = ["h","e","l","l","o"]

reverseString(s)
print(s)

