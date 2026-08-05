class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for n,f in count.items():

            bucket[f].append(n)


        ans = []
        for i in range(len(bucket)-1,0,-1):    
            for num in bucket[i]:
                ans.append(num)

                if (len(ans) == k):
                    return ans;

        