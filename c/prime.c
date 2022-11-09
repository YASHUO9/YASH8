#include <stdio.h>
int main()
{
    int i;
    printf("Enter the number  to check it is  prime");
    scanf("%d", &i);
    
    // if (i == 1)
    // {
    //     printf("This number is  prime");
        
    // }


    if(i%2 == 0 || i%3 ==0 || i%5 ==0 || i%7 ==0 || i % 11 == 0)
    {
        printf("This number is not prime");
    }
    else
    {
        printf("This number is prime");
    }
}







