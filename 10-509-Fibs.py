

def fib(n):

        def recurse(fibN):
            if fibN == 0 or fibN == 1:
                return fibN

            curr = recurse(fibN - 2) + recurse(fibN - 1)

            return curr

        return recurse(n)
        
n = 2
# Output: 1

print(fib(n))

