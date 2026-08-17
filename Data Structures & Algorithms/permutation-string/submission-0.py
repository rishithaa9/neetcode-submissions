class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1=len(s1)
        left=0
        if len(s1)>len(s2):
            return False
        
        count_s2={}
        for i in range(len_s1):
            c = s2[i]
            if c in count_s2:
                count_s2[c] += 1
            else:
                count_s2[c] = 1
        count_s1={}
        for i in s1:
            count_s1[i]=count_s1.get(i,0)+1
        if count_s1==count_s2:
            return True
        for right in range(len_s1, len(s2)):
            count_s2[s2[right]]=count_s2.get(s2[right],0)+1
            count_s2[s2[left]]-=1
            if count_s2[s2[left]]==0:
                del count_s2[s2[left]]
            left+=1
            if count_s1==count_s2:
                return True
        return False
