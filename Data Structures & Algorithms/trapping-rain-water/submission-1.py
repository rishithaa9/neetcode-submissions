class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefix=[0]*n
        suffix=[0]*n
        total=0
        prefix[0] = height[0]
        suffix[n-1] = height[n-1]
        for i in range(n):
            if height[i] > prefix[i-1]:
                prefix[i] = height[i]

            else:
                prefix[i] = prefix[i-1]

        for i in range(n-2, -1, -1):
            if height[i] > suffix[i+1] :
                suffix[i]=height[i]
            else:
                suffix[i] = suffix[i+1]

        for i in range(n):
            total+=min(prefix[i],suffix[i])-height[i]
        return total      