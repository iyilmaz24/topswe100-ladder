

def fizzBuzz(n: int):

        output = []
        for i in range(1, n + 1):
            if(i % 3 == 0 and i % 5 == 0):
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(f"{i}")

        return output

n = 3
# Output: ["1","2","Fizz"]

print(fizzBuzz(n))

