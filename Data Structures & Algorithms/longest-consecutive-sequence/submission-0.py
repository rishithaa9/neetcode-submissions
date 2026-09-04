class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        
        max_length=0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                current=i
                length=1
            while current+1 in nums:
                current=current+1
                length+=1

            max_length=max(length,max_length)

        return max_length


        