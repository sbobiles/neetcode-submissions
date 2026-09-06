class Solution {
    public boolean isAnagram(String s, String t) {
        //non optimal

        /*
        brute force:
        - nested for loop and keep counter for how many and tons of comparator operations

        - hashmap
        - make hashmap for both strings
        - traverse and add it to hashmap
        - if key exists, add to value (represents amt of char)
        - compare keys 
        */

        Hashtable<Character, Integer> str1 = new Hashtable<Character, Integer>();
        Hashtable<Character, Integer> str2 = new Hashtable<Character, Integer>();

        int currVal; 

        /*
        for(int i =0; i < s.length(); i++){
            if(str1.get(s.charAt(i)) == null){
                str1.put(s.charAt(i), 1);
            }
            else{
                currVal = str1.get(s.charAt(i));
                str1.put(s.charAt(i), ++currVal);
            }
        }

        for(int i = 0; i < t.length(); i++){
            if(str2.get(t.charAt(i)) == null){
                str2.put(t.charAt(i), 1);
            }
            else{
                currVal = str2.get(t.charAt(i));
                str2.put(t.charAt(i), ++currVal);
            }
        }
        */

        // ^ combined for loops

        if(s.length() != t.length()){
            return false;
        }

        for(int i = 0; i < s.length(); i++){
            str1.put(s.charAt(i), str1.getOrDefault(s.charAt(i), 0) + 1);
            str2.put(t.charAt(i), str2.getOrDefault(t.charAt(i), 0) + 1);
        }

        return str1.equals(str2);

    }
}
