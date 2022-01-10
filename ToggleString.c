
// You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

// Input Format
// The first and only line of input contains the String S

// Output Format
// Print the resultant String on a single line.

// Sample Input
// abcdE
// Sample Output
// ABCDe

#include <stdio.h>

int main()
{
    char a[100],i=0;
	printf("Enter a string: ");
    scanf("%s",a);
    for(i=0;a[i]!='\0';i++)
    {
    	if(a[i] >= 'a' && a[i] <= 'z')
    	{
    		a[i] = a[i]-32;
    	}
    	else if(a[i] >= 'A' && a[i] <= 'Z')
    	{
    		a[i] = a[i] +32;
    	}
    }
    printf("%s",a);
    return 0;
	
}