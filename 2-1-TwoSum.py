

def twoSum(nums):  
    dictN = {}
    for index, num in enumerate(nums):
        targ = target - num
        if targ in dictN:
            return (dictN[targ], index)
        else:
            dictN[num] = index

nums = [2,7,11,15]
target = 9

print(twoSum(nums))

