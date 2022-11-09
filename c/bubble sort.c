#include <stdio.h>
int main()
{
    int n,i,array[5] = {7,2,8,4,1},j,temp;
    printf("\n enter the size of the array ");
    scanf("%d",&n);

    printf("yash pathak\n");
    for(i=0;i<n-1;i++) //pass 
    {
        for(j=0;j<n-1;j++)
        {
            if (array[j]=array[j+1])
            {

                temp = array[j];
                array[j]=array[j+1];
                array[j+1]=temp;
            }
        }
    }
}