#include <stdio.h>

int main(void) {
    int t, x,y;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &x, &y);
        if(x<y) printf("no\n");
        else printf("yes\n");    }
	// your code goes here
	return 0;
}
