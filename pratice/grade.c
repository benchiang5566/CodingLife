/*
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	
	printf("\n=========before=======\n");

	int i,student_grades[60];
	int lowest=-1,hightest=60;
	
	srand(time(NULL));
	
	for(i=0;i<60;i++){
		
		student_grades[i] = rand() % 60;
		
		if(student_grades[i] > hightest){

			hightest = student_grades[i];
		}
		if(student_grades[i] < lowest){

			lowest = student_grades[i];
		}
		printf("%d\t",student_grades[i]);
	}

	printf("\n======after==========\n");

	for(i=0;i<60;i++){

		printf("%.f\t",60+40.0*(student_grades[i]-lowest)/(hightest-lowest));
	}

	return 0;
}
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int x;
    int i, g[60];
    int m = -1, M = 101;
    
    // Initialize random seed using current time for better randomness
	//瘋狂程設不用寫
    srand(time(NULL));
    printf("\n\n======before=========\n\n");

    for(i = 0; i < 60; i++) {
        // Generate random number between 0 and 100
        x = rand() % 101;
        g[i] = x;
        
        if(x > m) m = x;
        if(x < M) M = x;

		printf("%d\t",g[i]);
	}
    printf("\n\n========after=========\n\n");

    // Make sure we don't divide by zero if all numbers are the same
    /*if(m == M) {
        for(i = 0; i < 60; i++) {

            printf("%.f\t", 80.0); // Output middle of the range if all values are equal
        
			}
    }*/ 
	//else {
        for(i = 0; i < 60; i++) {

            printf("%.1f\t", 60 + 40.0 * (g[i] - m) / (M - m));
			
        }
    //}
    
    return 0;
}