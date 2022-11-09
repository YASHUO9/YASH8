#include <stdio.h>
int main(){
    int a;
    printf("Enter the marks");
    scanf("%d",&a);
    if (a<50)
    printf(" F grade\n");
    else if(a>= 50 && a <60)
    printf(" D grade\n");
    else if(a>= 60 && a <70)
    printf(" C grade\n");
    else if(a>= 70 && a <80)
    printf(" B grade\n");
    else if(a>= 80 && a <90)
    printf(" A grade\n");
    else 
    printf("O grade\n");
    return 0;
}