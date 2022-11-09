#include <stdio.h>
int main(){
    int i,j,k;
    printf("Enter the 3 number ?");
    scanf("%d",&i);
    scanf("%d",&j);
    scanf("%d",&k);
    if (i>k && k >j)
    printf("1st number is greater");
    else if(j>k && k>i)
    printf("2nd number is greater");
    else
    printf("3rd number is greater");
    return 0;

    
}