class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultsList = []
        iterator = 0;
        for x in range(len(nums)):
            print("x= ", x)
            for y in range(x+1, len(nums)):
                if(nums[x]+nums[y] == target):
                    result = [x, y]
                    return result

            

