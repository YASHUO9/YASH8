#include <stdio.h> 
char fun();  //function declaration 
void main()
{
    char ch;
    ch=fun();
    printf("ch=%c", ch);
    //function calling
  }
  char fun()
{ 
    char c;  // function definition
    printf("enter the character\n"); 
    scanf("%c",&c);
    
    return 'c';// if we replace the 'c' by the c then we get the same answer as we entered character else we don;t change we get c only as output
 }