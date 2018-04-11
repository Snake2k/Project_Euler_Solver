import java.util.*;

public class q10{

    public static void main(String args[]){
        
        long serial = 5;
        long ans = 0;
        boolean mod = false;

        for(int a=3;a<2000000;a+=2){

            for(int b=3;b<a;b+=2){
                if((a%b) != 0){
                    mod = true;
                }else{
                    mod = false;
                    break;
                }
            }
            if(mod){
                serial+=a;
                mod = false;
            }
        }
        System.out.println(serial);
    }
}
