class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts={}
        countt={}
        for i in s:
            if i not in counts:
                counts[i]=1
            else:
                counts[i]+=1
        for i in t:
            if i not in countt:
                countt[i]=1
            else:
                countt[i]+=1

        return counts==countt