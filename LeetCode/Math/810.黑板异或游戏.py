class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        n = len(nums)
        #偶数先手必胜
        if n % 2 == 0:
            return True
        #先手结束以后剩余的值异或为0
        return reduce(xor,nums) == 0
        
