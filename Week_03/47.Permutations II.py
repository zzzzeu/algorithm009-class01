class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(nums, temp):
            if nums == []:
                res.append(temp)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]: 
                    continue           
                back(nums[:i] + nums[i + 1:], temp + [nums[i]])
        back(nums,[])
        return res