#include<stdio.h>
int main()
{
    int a,b,c;
    printf("Enter the number:");
    scanf("%d",&a);
    b=a%10;
    c=a/10;
    printf("%d",b);
    printf("%d",c);
    return 0;
}