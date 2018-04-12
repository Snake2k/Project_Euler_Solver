import java.util.*;

public class q4{
    
    public static void main(String[] args){
        int val=0;
        int ans=0;
        String norm, rev;

        for(int a=100;a<1000;a++){
            for(int b=100;b<a;b++){
                val = a*b;
                norm = String.valueOf(val);
                rev = new StringBuilder(norm).reverse().toString();
               // System.out.println(a + "----" + b + "----" + val + "----" + norm + "----" + rev);
                if(norm.equals(rev) && val > ans ){
                    ans = val;
                }
            }
        }

        System.out.println(ans);
    }
}
