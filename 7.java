class Solution {
    public int reverse(int x) {
        String s="";
        for(int i=0;i<(""+Math.abs(x)).length();i++){
            s=(""+Math.abs(x)).charAt(i)+s;
        }
        try{
            if(x<0) return Integer.parseInt("-"+s);
            else return Integer.parseInt(s);
        }catch(Exception e){
            return 0;
        }
    }
}
