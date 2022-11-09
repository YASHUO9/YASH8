#include <stdio.h>

int main()
{
    int *ptrA;
    float *ptrB;
    
    ptrA = (int *)1000;       // pointer comparison of different type of pointer
    ptrB = (float *)2000;
    
    if(ptrB > ptrA)
       printf("PtrB is greater than ptrA\n");
       printf("Yash\n");
    
    return(0);
}