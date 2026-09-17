class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(numbers)):
            needed=target-numbers[i]
            if needed in dict1:
                return [dict1[needed]+1,i+1]
            dict1[numbers[i]]=i