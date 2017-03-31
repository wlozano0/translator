#include <stdio.h> 

void f1(var1){
	printf("Total is: %d\n", var1);
}

void main(){
	int var1 = 3;
	int var2 = 4;
	int var3 = 5;

	var3 = var1 + var2;

	f1(var3);
}
