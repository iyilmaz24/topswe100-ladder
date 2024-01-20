

def isAnagram(s, t):
        s.replace(" ", "")
        t.replace(" ", "")

        return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"

print(isAnagram(s, t))

