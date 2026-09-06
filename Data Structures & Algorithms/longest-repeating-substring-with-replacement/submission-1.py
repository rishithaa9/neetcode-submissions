class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_len = 0
        count={}
        max_f=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0) + 1 
            max_f = max(max_f, max(count.values()))
            while (right-left+1) - max_f > k:
                count[s[left]]-=1
                if count[s[left]]==0:
                    del count[s[left]]

                left+=1
            max_len=max(max_len,right-left+1)
        return max_len

            