import java.util.*;

public class q9{
    public static void main(String args[]){

        int a=0;
        int b=0;
        int c=0;

        for(int x=1;x<1000;x++){
            for(int y=x+1;y<1000;y++){
                int z = 1000 - x - y;
                if(x*x+y*y==z*z){
                    a=x;
                    b=y;
                    c=z;
                    break;
                }
            }
        }

        System.out.println(a*b*c);
    }
}
