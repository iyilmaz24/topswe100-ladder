

def isPowerOfThree(n):
        if n == 1:
            return True
        if n < 3:
            return False
        
        while n >= 3:
            n = n / 3

        return n == 1


n = 27
# Output: true

print(isPowerOfThree(n))

