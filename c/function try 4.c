#include <stdio.h> 
float sum(); // function declaration  as float type if we not write this program will not run in case of float but run in case of integer type instead
void main()
{ sum();    //function calling
printf("\n");
 sum();
 printf("\n");
 printf("hello world\n"); }
  float sum()
{ 
    float a,b,sum;  // function definition
    printf("enter the number\n"); 
    scanf("%f %f",&a,&b);
    sum= a+b;
    printf("\n sum is %f",sum);
 }