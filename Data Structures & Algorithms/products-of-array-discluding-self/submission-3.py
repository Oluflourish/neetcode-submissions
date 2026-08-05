class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nz = []
        for i, n in enumerate(nums):
            if n != 0:
                nz.append([i,n])
        print(nz)

        product = 1
        if len(nz) < len(nums):
            for n in nz:
                product *= n[1]
        else: 
            for n in nums:
                product *= n
        
        if len(nz) == 0:
            product = 0
        print('product', product)

        res = []
        zero_count = len(nums) - len(nz) 
        if zero_count > 1: return [0] * len(nums)

        if zero_count == 1:
            res = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = product
            return res        
        
        for n in nums:
            res.append(int(product/n))
        
        return res