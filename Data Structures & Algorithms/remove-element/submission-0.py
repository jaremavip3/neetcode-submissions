class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        acc = 0
        for x in range(nums.count(val)):
            nums.remove(val)
            nums.append("_")
            acc += 1
            

  
        print(nums)
        return len(nums)-acc;
