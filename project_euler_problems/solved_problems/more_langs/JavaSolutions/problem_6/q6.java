import java.util.*;

public class q6{

    public static void main(String args[]){
        int first=0;
        int second=0;
        int ans=0;

        for(int a=0;a<=100;a++){
            first += (a*a);
        }

        for(int b=0;b<=100;b++){
            second += b;
        }
        second = (second*second);
        ans = Math.abs(second - first);

        System.out.println(ans);
    }
}
