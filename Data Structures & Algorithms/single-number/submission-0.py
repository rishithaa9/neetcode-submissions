class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1

        for key,val in count.items():
            if val==1:
                return key
        