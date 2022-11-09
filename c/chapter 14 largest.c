/*Pick up largest number from 5*5 matrix*/
#include <stdio.h>
int main()
{
    int a[5][5]={1,2,3,4,5,6,7,8,9,99,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25},i,j,big;
   // big=a[0][0];
    big=0;
    for(i=0;i<5;i++)
    {
        for(j=0;j<5;j++)
        {
            if(a[i][j]>big)
            big=a[i][j];
        }
    }
    printf("\nLargest number in the matrix is %d\n",big);
    return 0;
}