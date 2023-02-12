#include <stdio.h>

int main(void) {
    
    int t, x, y;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d", &x,&y);
        if(x>10*y) printf("yes\n");
        else printf("No\n");
    }
    // your code goes here
    return 0;
}