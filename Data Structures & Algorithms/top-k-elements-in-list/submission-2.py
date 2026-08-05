class Solution:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        unique = set(nums)
        res = []
        
        for u in unique:
            count = nums.count(u)
            if count >= k:
                res.append(u)
        return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = set(nums)
        res = []
        
        for u in unique:
            count = nums.count(u)
            res.append([count, u])

        res.sort(reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(res[i][1])

        return ans




              
            

        



