# include <stdio.h>
 int main()
 {
     int i;
     printf("\n enter the day of week in number  1to 7");
     scanf("%d",&i);
     if(i==1)
     printf("\n the day is sunday\n");
     else if(i==2)
     printf("\n the day is monday\n");
     else if(i==3)
     printf("\n the day is tuesday\n");
     else if(i==4)
     printf("\n the day is wednesday\n");
     else if(i==5)
     printf("\n the day is thursday\n");
     else if(i==6)
     printf("\n the day is friday\n");
     else
     printf("\n the day is saturday\n");
     return 0;
 }