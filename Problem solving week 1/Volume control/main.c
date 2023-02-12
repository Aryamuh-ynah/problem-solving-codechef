#include <stdio.h>

int main(void) {
    int t, x,z;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &x, &z);
        printf("%d\n", abs(x-z));
    }
	// your code goes here
	return 0;
}
