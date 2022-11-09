
#include <stdio.h>
int main()
{
   int k ,unit;
   printf("Enter unit Consured");
   scanf("%d", &unit);

double m = 0.0;

if(unit < 100)
{
m= 2.50 * unit;
}
else if (unit >= 100 && unit <200)
{  m = 100* 2.50 +(unit - 100) * 3.50;}

else if (unit >= 200 && unit < 200)
m = 100* 2.50 + 100 * 3.50 +(unit-200) + 4.50;
else
m= 100*2.50 + 100 * 3.50 + 100 * 4.50 + (unit-300)*550;
printf(" bill consumed = %f ", m);
}