#include<stdio.h>  
 int main()  
 {  
 int N,i,fact;  
 fact=1; 
 printf("Enter a number: \n") ;
 scanf("%d",&N);  
 for(i=1;i<=N;i++)  
 {  
 fact=fact*i;  
 }  
 printf("%d",fact);  
 return 0;  
 }  