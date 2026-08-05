class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = set(nums)
        res = []
        
        for u in unique:
            count = nums.count(u)
            res.append([count, u])

        print(res)

        res.sort(reverse=True)

        print(res)
        
        ans = []
        for i in range(k):
            ans.append(res[i][1])

        return ans




              
            

        



