///week09-3.cpp

#include <stdio.h>
#include <algorithm> ///�I�s�禡
#include <vector> ///�I�s�禡
using namespace std; ///C++
int main(){

	vector<int> a(100); ///C++�}�C�ŧi��ܪk

	for(int i=0; i<100; i++){
		scanf("%d", &a[i]);
	}

	std::sort(a.begin(), a.end()); /// �W�ŧֱƧǪk

	for(int i=0; i<100; i++){
		printf("%d ", a[i]);
	}
}
