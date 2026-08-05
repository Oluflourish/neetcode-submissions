class Solution:
    def twoSumA(self, nums: List[int], target: int) -> List[int]:
        A = []

        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
            
            elif curr > target:
                j = j - 1
            
            elif target > curr:
                i = i + 1

            else:
                return []

    
    
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