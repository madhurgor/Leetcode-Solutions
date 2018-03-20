class Solution {
    public boolean isPalindrome(int x) {
        String temp=""+x;
        for(int i=0;i<temp.length();i++){
            if(temp.charAt(i)==temp.charAt(temp.length()-i-1)){
               continue; 
            }else{
                return false;
            }
        }
        return true;
    }
}
