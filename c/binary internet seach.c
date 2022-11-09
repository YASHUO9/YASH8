#include <stdio.h>
int main() { int a[5],i,n,x,flag=0,first,last,mid;
    printf("\n enter the size of the array\n");
    scanf("%d",&n);
    printf("\n enter the array in the ascending order ");
    for (int i = 0; i < n; i++)
    scanf("%d",&a[i]);
    printf("\n enter the element to search in the array ");
    scanf("%d",&x);


    first = 0;
    last = n-1;
    while (first <= last)
    {
        mid= (first + last)/2;
        if(x==a[mid])
        {
              flag=1;
              break;
          }
        else if(x>a[mid])
        first=mid +1;
        else
          last =mid -1;
          
    }
  if(flag==1)
  printf("\n element found at position ::%d",mid+1);
  else 
  printf("\n element  is not found at position ::%d",mid);
  return 0;
}