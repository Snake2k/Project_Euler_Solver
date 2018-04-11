import java.util.*;

public class q5{
    
    public static void main(String args[]){

        boolean done = false;
        int a=1;
        int ans=0;

        while(done==false){
            for(int b=1;b<=20;b++){
                if(a%b == 0){
                    ans = a;
                    done = true;
                }else{
                    done = false;
                    break;
                }
            }
            if(done == true){
                System.out.println(ans);
                break;
            }
            a++;
        }
    }
}
