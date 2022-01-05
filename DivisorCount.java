/*You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k.
 You do not need to print these numbers, you just have to find their count.
SAMPLE INPUT
1 10 1
SAMPLE OUTPUT
10 */

import java.util.*;
import java.util.Scanner;
public class DivisorCount {
    
    public static void main(String args[] ) throws Exception {
     
        //Scanner
        Scanner s = new Scanner(System.in);
        System.out.println("To find divisor\nFrom: ");
        int l = s.nextInt();
        System.out.println("To: ");
        int r = s.nextInt();
        System.out.println("Enter the number you want to find divisor: ");
        int k = s.nextInt();
        int count=0;

        for (int i = l; i <=r; i++) {
            if(i%k==0){
                count++;
            }
        }


        System.out.println(count);
    }
}
