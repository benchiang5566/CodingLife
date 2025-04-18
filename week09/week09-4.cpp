/// week00-4.cpp

#include <stdio.h>

int main(){
	int n;
	scanf("%d", &n);

	for(int i=1; i<=n; i++){ ///確定好星星蓋幾層
		for(int j=1; j<=i; j++){ ///再跑第N層，有第N個星星
			printf("*");
		}
		printf("\n");
	}
}
