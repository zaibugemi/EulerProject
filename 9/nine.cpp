#include <iostream>
#include <math.h>
using namespace std;

int pythagoreanTripletProduct(int sum) {
	int c;
	for (int a = 1; a < sum /2 ; a++){
		for (int b = a + 1; b < sum; b++){
			c = sum - a - b;
			if ( pow(a,2) + pow(b,2) == pow(c,2) ){
				return a*b*c;
			}
		}
	}
}





int main() {
	cout<<pythagoreanTripletProduct(1000);

	return 0;
}