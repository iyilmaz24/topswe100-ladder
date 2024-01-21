

# Calculate the sum of the elements of nums between indices left 
# and right inclusive where left <= right.

class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sumR = 0
        for num in self.nums[left:right+1]:
            sumR += num
        return sumR
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
    
