class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        min_length = float('inf')
        curr=0
        for right in range(len(nums)):
            curr+=nums[right]

            while curr>=target:
                curr-=nums[left]
                min_length=min(min_length,right-left+1)
                left+=1
                
        if min_length==float('inf'):
            return 0
        return min_length
        