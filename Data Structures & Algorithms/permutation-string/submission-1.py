class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        counts1 = {}
        counts2 = {}
        left = 0
        if m > n:
            return False
        for i in s1:
            counts1[i] = counts1.get(i, 0) + 1
        window=s2[:m]
        
        for i in window:
            counts2[i] = counts2.get(i, 0)+ 1

        if counts2 == counts1:
            return True

        for right in range(m,n):
            counts2[s2[right]] = counts2.get(s2[right], 0) + 1
            counts2[s2[left]] -= 1
            if counts2[s2[left]]==0:
                del counts2[s2[left]]

            left+=1
            if counts1 == counts2:
                return True

        return False

            
                






        