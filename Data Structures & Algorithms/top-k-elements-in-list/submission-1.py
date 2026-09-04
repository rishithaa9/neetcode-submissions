class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        ot=[]
        for i in nums:
            count[i]=count.get(i,0)+1
        res=[[] for i in range(len(nums)+1)]
        for key,values in count.items():
            res[values].append(key)
        for i in range(len(res)-1,-1,-1):
            if res[i]:
                for n in res[i]:
                    ot.append(n)
                    if len(ot)==k:
                        return ot
            
