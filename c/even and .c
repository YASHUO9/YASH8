#include <stdio.h>
int main ()
{
    int i,j,k;
    do{
        printf("enter the number \n");
        scanf("%d",&i);
        if (i%2 == 0)
        printf("the number is even\n");
        else 
        printf(" number is odd\n");
        printf(" would you wish to check again type 1 for Yes or  0 for No?\n");
        scanf("%d",&j);}
    while(j==1);
    return 0;
    
}