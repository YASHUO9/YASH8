#include <stdio.h>
int main()
{   int i,n,a[5],search,first,last,mid;
    printf("\n enter the size of the array\n");
    scanf("%d", &n);
    printf("\n enter the number of elements in the array\n");
    for (int i = 0; i < n; i++)
    {
        printf("\n the %d element of the array is::",i+1);
        scanf("%d", &a[i]);
    }
     printf("\n enter the element to search in the array");
     scanf("%d", &search);
     first = 0;
     last = n - 1;
     while(first <= last)
     {   if(a[mid] < search) 
         first = mid + 1;
         else if(a[mid] == search) 
         {printf("\n%d found at location %d",search,mid + 1);
         break;}
         else
         last = mid - 1;
         mid =(first + last)/2;
         
         if(first>last)
          printf("\n %d is not foundat location ", search);

     }
}