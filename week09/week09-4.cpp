/// week00-4.cpp

#include <stdio.h>

int main(){
	int n;
	scanf("%d", &n);

	for(int i=1; i<=n; i++){ ///�T�w�n�P�P�\�X�h
		for(int j=1; j<=i; j++){ ///�A�]��N�h�A����N�ӬP�P
			printf("*");
		}
		printf("\n");
	}
}
