class Solution {
    public int lengthOfLongestSubstring(String s) {
        /*
        // brute force
        String r="";
        int c=0,max=0;
        for(int i=0;i<s.length();i++){
            r=""+s.charAt(i);
            c=1;
            for(int j=i+1;j<s.length();j++){
                if(r.indexOf(s.charAt(j))==-1){
                    r+=""+s.charAt(j);
                    c++;
                }else{
                    break;
                }
            }
            if(max<c){
                max=c;
            }
        }
        return max;*/
        
        // optimized
        HashSet<Character> hs=new HashSet<Character>();
        int max=0,c=0;
        for(int i=0;i<s.length();i++){
            if(hs.contains(s.charAt(i))){
                hs.remove(s.charAt(i));
                //System.out.println(s.substring(i-c,i));
                //System.out.println(s.substring(i-c,i).indexOf(s.charAt(i)));
                i=i-c+s.substring(i-c,i).indexOf(s.charAt(i));
                //System.out.println(i);
                hs.clear();
                if(max<c){
                    max=c;
                }
                c=0;
            }else{
                c++;
                hs.add(s.charAt(i));
                //System.out.println(c);
            }
        }
        if(max<c)
            max=c;
        return max;
    }
}

/*
hashset iterator
Iterator<Character> it = hs.iterator();
while(it.hasNext()){
    System.out.println(it.next());
}*/
