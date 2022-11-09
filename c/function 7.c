#include <stdio.h> 
 void sum();// this is known as declaration of function if it is not written then the prg will run but givng the implicit function type error 
 void main() //calling function
{ sum();
 printf("\n");
 sum();
 printf("\n");
 printf("hello world\n"); }
  void sum()    // definition of function
{ 
    int a,b,sum;
    printf("enter the number\n"); 
    scanf("%d %d",&a,&b);
    sum= a+b;
    printf("\n sum is %d",sum);
 }
