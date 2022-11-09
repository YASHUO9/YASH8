#include <stdio.h>
int main()
{
    int a[5],i,j,k,l=0,r,data;
    printf("\nenter the size of the array ");
    scanf("%d",&j);
    printf(" \nenter the element of the array in ascending order");
    for(i=0;i<j;i++)
    {
        printf(" \nthe %d element of the array is",i+1);
        scanf("%d",&a[i]);
    }
    printf(" enter the element to search \n");
    scanf("%d", &k);
    l=0;
    r=j-1;
    while(l<=r)
    { i =(l+r)/2;
       if(k ==a[i])
       return i;
       else if(k<<a[i])
       r=  i+1;
       else
       l=i+1;
       }
       return 0;
}