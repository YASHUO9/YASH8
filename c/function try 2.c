#include <stdio.h> 
void sum();  //function declaration 
void main()
{ sum();    //function calling
printf("\n");
 sum();
 printf("\n");
 printf("hello world\n"); }
  void sum()
{ 
    int a,b,sum;  // function definition
    printf("enter the number\n"); 
    scanf("%d %d",&a,&b);
    sum= a+b;
    printf("\n sum is %d",sum);
 }
 