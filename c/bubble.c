#include <stdio.h>
int main()
{
    int n,i,array[5],j,temp;
    printf("\n enter the size of the array\n");
    scanf("%d",&n);
    printf("\n enter the element of the array ");
    for(i=0;i<n;i++)
    {printf(" %d element of the array ",i+1);
    scanf("%d",&array[i]);
    }
    printf("yash pathak\n");
    for(i=0;i<n-1;i++) //pass 
    {
        for(j=0;j<n-1;j++)
        {
            if (array[j]>array[j+1])
            {

                temp = array[j];
                array[j]=array[j+1];
                array[j+1]=temp;
            }
        }
    }
    printf("array after implementing bubble sort:");
    for (int i=0; i<n;i++)
    {printf("%d ",array[i]);}
    return 0;
}