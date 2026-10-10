class Solution {
    public boolean hasDuplicate(int[] nums) {
        //not optimal solution
        //time complexity: n^2

        //vars
        boolean dup = false;

        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j < nums.length; j++){
                if(nums[i] == nums[j] && i != j){
                    dup = true;
                }
            }
        }

        return dup;
        
    }
}