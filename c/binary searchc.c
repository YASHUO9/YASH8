#include<stdio.h>
int main()
{ int data,i,l,n,a[i],mid;
    printf("\nenter the array size");
    scanf("%d", &n);
    printf("\n enter the array element int he ascending order ");
    for (int i = 0; i < n; i++)
 {  
     printf("\n enter the %d element of the array ", i+1);
     scanf("%d", &a[i]);
}
    print("\n enter the element to  seach in the array ");
    scanf("%d", &data);
    l==0;
    r==n-1;
    while(l<=r)
    { 
        mid = (l+r)/2;
        if(data==a[mid]);
        return mid;
        else if(data<a[mid])
        r=mid-1;
        elsel=mid+1;
    
    }
     return -1;



}