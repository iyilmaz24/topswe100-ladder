

def hammingWeight(n):
        
        count = 0
        for char in str(bin(n)):
            if char == "1":
                count += 1

        return count


n = 11

print(hammingWeight(n))

