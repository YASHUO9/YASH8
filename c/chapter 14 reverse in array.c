/*program to copy one array into another in reverse order*/
#include <stdio.h>
int main ()
{
    int a[2][2],b[2][2],i,j,n;
    printf("enter the size of the array");
    scanf("%d",&n);
    for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            printf("\n the element of the array is: ");
            scanf("%d",&a[i][j]);
        }
    }
    
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
        a[i][j] =b[i][j];                  
        }
    }
    printf("\n the copied array in reversed order:");
    printf("\n");
    for(i=4;i>0;i--)
    {
        for(j=4;j>0;j--)
        {
            printf("%d\t",b[i][j]);
        }
        printf("\n");
    }
    return 0;
}