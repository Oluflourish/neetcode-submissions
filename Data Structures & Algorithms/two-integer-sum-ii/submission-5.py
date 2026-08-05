class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = len(numbers)
        i = 0
        j = n - 1 

        while 1:
            if numbers[i]+numbers[j] > target: 
                j -= 1 
                continue
            elif numbers[i]+numbers[j] < target: 
                i += 1
                continue
            else: 
                print (numbers[i],numbers[j])
                return [i+1, j+1]

        return []


