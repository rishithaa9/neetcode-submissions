class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for val in count.values():
            if val>1:
                return True
        return False 
        