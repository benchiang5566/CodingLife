///week09-3.cpp

#include <stdio.h>
#include <algorithm> ///呼叫函式
#include <vector> ///呼叫函式
using namespace std; ///C++
int main(){

	vector<int> a(100); ///C++陣列宣告表示法

	for(int i=0; i<100; i++){
		scanf("%d", &a[i]);
	}

	std::sort(a.begin(), a.end()); /// 超級快排序法

	for(int i=0; i<100; i++){
		printf("%d ", a[i]);
	}
}
