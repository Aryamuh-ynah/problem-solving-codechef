#include <stdio.h>

int main(void) {
    int x;
    scanf("%d", &x);
    int a,b;
    //printf("Enter two cab service charges: ");
    while(x--)
    {
    scanf("%d%d", &a, &b);
    if(a>b)
    {
        printf("SECOND\n");
        
    }
    else if(b>a)
    {
        printf("FIRST\n");
    }
    else
    {
        printf("ANY\n");
    }
    }
	// your code goes here
	return 0;
}
