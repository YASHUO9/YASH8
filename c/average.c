#include <stdio.h>
int main(){
    int i,n,a[100],sum=0;
    printf("Enter the total number you want to find the average ?\n");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for (i=0;i<n;i++)
    {
        sum += a[i];
    }
    sum/2;
    if (sum <0)
    {
        printf("sum is negative \n");
    }
    else
    {
        printf("sum = %d", sum/2);
    }
}