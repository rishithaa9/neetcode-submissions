class Solution {
    public int maxSubArray(int[] nums) {
        int sums=0;
        int maxs=Integer.MIN_VALUE;

        for (int x: nums){
            sums=sums+x;
            maxs=Math.max(maxs,sums);
            if (sums<0){
                sums=0;
            }
        }
        return maxs;
        
    }
}
