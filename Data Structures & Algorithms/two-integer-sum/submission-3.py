class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums2 = nums
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            nums2[i] = -1000000000 
            
            if diff in nums2:
                res.append(i)
                res.append(nums2.index(diff))
                break
            
            nums2 = nums 
                
        return list(set(res))