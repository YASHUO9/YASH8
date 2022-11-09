 #include<stdio.h>
 int sum(int a,int b);// return type,name of the function(types of the arguments or data type)  
 // if i use the data type 'int' than use the same as defination one
 void main()
 {
     sum(1,8);
     sum(2,8);
     sum(1,4);
 }
 
 int sum(int x,int y)
{ 
    int sum = 0;//defination if use void than both void
  //  printf("enter the number\n"); 
   // scanf("%d %d",&a,&b);
    sum= x+y;
    printf("\n sum is %d",sum);
 }