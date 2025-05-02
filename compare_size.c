#include <stdio.h>

int main(){
    int a, b, c;
    
    scanf("%d%d%d", &a, &b, &c);
    int max=0, min=0;
    max = a>b ? (a>c ? a:c) : (b>c ? b:c);
    min = a<b ? (a<c ? a:c) : (b<c ? b:c);

    printf("%d-%d=%d\n",max, min, max - min);
    return 0;
}
