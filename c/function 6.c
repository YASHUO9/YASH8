#include <stdio.h>

void sum()
 {

    int a;
    printf("the number to check");
    scanf("%d", &a);
    if (a%2==0)
    printf("the number  is even");
    else
    printf("the number is odd");

}
void main()
{
    sum();
    printf("the hello world");
    sum();
}