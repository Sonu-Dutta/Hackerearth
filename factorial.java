
/*
You have been given a positive integer N. You need to find and print the Factorial of this number. 
The Factorial of a positive integer N refers to the product of all number in the range from 1 to N. 
You can read more about the factorial of a number here.
*/
import java.util.*;
import java.util.Scanner;
public class factorial {
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number: ");
    int i, fact=1;
    int number=sc.nextInt();

    for(i=1;i<=number;i++){
        fact=fact*i;
    }
    System.out.println("Factorial of "+number+ " is "+fact);
    }
}
