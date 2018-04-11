import java.util.*;

public class q7{

    public static void main(String args[]){
        
        int serial = 1;
        int ans = 0;
        boolean mod = false;

        for(int a=3;;a++){

            for(int b=2;b<a;b++){
                if((a%b) != 0){
                    mod = true;
                }else{
                    mod = false;
                    break;
                }
            }
            if(mod){
                serial++;
                mod = false;
                if(serial == 10001){
                    ans = a;
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}
