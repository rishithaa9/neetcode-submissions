class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_length=0
        count={}
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]]+=1
            else:
                count[s[right]]=1
            max_f=0
            max_f=max(max_f, max(count.values()))
            while (right-left+1)-max_f >k:
                count[s[left]]-=1
                if count[s[left]]==0:
                    del count[s[left]]
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length



