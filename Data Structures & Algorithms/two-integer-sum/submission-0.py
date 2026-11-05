class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indici = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in indici:
                return [indici[diff],i]
            indici[n] = i