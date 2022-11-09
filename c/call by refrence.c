#include <stdio.h>

void fun(int*,int*);
void main()
{
    int x=5,y=7;
    fun(&x,&y);
    printf("inside main(calling function)\n");
    printf("x=%d y=%d\n",x,y);

}
   void fun(int* a,int* b)
{ 
    *a = 7;
    *b = 5;
    printf("a=%d b=%d\n",*a,*b);
}