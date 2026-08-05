class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        
        res = 0 
        for d in data:
            count = 1
            if d-1 in data: continue
            else:
                i = 1
                while 1:
                    if d+i in data: 
                        count += 1
                        i += 1
                    else: break
            if count > res: res = count
        
        return res


            

        


        