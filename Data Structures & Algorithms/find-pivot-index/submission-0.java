class Solution {
    public int pivotIndex(int[] nums) {
        int n=nums.length;
        int[] ls= new int[n];
        ls[0] = nums[0];
        int[] rs=new int[n];
        rs[n-1]= nums[n-1];
        for (int i=1;i<n;i++){
            ls[i]=ls[i-1]+nums[i];
        }
        for (int i=n-2;i>=0;i--){
            rs[i]=rs[i+1]+nums[i];
        }
        for (int i=0;i<n;i++){
            if (ls[i]-nums[i]==rs[i]-nums[i]){
                return i;
            }
        }
        return -1;
        
    }
}