/// week09-2.cpp

#include <stdio.h>

int main(){
	int a[100];
	for(int i=0; i<100; i++){
		scanf("%d", &a[i]);
	}

	for(int i=0; i<100; i++){ ///¿ï¾Ü±Æ§Çªk
		for(int j=i+1; j<100; j++){

			if(a[i]>a[j]){
				int temp=a[i];
				a[i]=a[j];
				a[j]=temp;

			}
		}
	}

	for(int i=0; i<100; i++){
		printf("%d", &a[i]);
	}
}
