class Solution {
    public boolean isPalindrome(String s) {
        //two pointer
        /*
            - while loop to traverse
            - If both pointers are equal then move ptrs
            - If unequal then return false
            - if it gets to end return true
        */

        String cleanS = (s.replaceAll("[^a-zA-Z0-9]", "")).toLowerCase();

        int i = 0;
        int j = cleanS.length()-1; 

        while(i < j){
            if(cleanS.charAt(i) != cleanS.charAt(j)){
                return false;
            }
            i++;
            j--;
        }

        if(i == j){
            if(cleanS.charAt(i) != cleanS.charAt(j)){
                return false;
            }
        }
        return true;
    }
}
