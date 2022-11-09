#include <stdio.h>
int main()
{   int mid,l,i,r,data,a[5],n;
    printf("enter the size of the of the array\n");
    scanf("%d", &n);
    printf("enter the number of elements of the array \n");
    for (int i = 0; i < n; i++)
    {printf("\n enter the%d element of the array\n", i+1 );
    scanf("%d", &a[i]);
    }
    printf(" enter the element of the array to search\n");
    scanf("%d", &data);
    l=0;
    r=n-1;
    mid =(l+r)/2;
    while (l <= r)
    { 
      if (data == a[mid])
       return mid;
       else if (data<a[mid])
       r=mid-1;
       else
       l=mid-1;
    }
    return 0;
    }