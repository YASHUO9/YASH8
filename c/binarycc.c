#include <stdio.h>
int main()
{
    int n,i,search,l,r,array[5],mid;
    printf("\n enter the size of the array\n");
    scanf("%d",&n);
    printf("\n enter the element of the array ");
    for(i=0;i<n;i++)
    {printf(" %d element of the array ",i+1);
    scanf("%d",&array[i]);
    }
    printf("\n enter the element to search in the array ");
    scanf("%d",&search); 
    l=0;
    r= n-1;
    mid =(l+r)/2;
    while(l<=r)
    {
        if(array[mid]< search)
        l =mid +1;
        else if(array[mid] == search)
        { printf(" %d fount at the location %d ", search,mid +1);
          break;}
          else 
          r =mid -1;
          mid =(l+r)/2;
    
    if(l>r)
    printf(" not found at the location \n");}
    return 0;
}