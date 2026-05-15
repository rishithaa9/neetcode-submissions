class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n=nums.length;
        int[] ls=new int[n];
        int[] rs=new int[n];
        int[] ans=new int[n];
        ls[0] = 1;
        rs[n-1]=1;
        for(int i=0;i<n-1;i++){
            ls[i+1]=ls[i]*nums[i];

        }
        for(int i=n-2; i>= 0; i--){
            rs[i]=rs[i+1]*nums[i+1];
        }
        for(int i=0;i< n;i++){
            ans[i]=ls[i]*rs[i];
        }
        return ans;
    }
}  
