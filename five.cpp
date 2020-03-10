// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#include <iostream>
using namespace std;

bool least_mulitple(int num, int divisor){
	if (divisor == 1){
		return true;
	}
	if (num % divisor == 0){
		return least_mulitple(num, divisor - 1);
	}
	else{
		return false;
	}
}

int main(){
	long long divisor;
	long long is_evenly_divisible = 0;
	cout<<"Enter the number: ";
	cin>>divisor;

	long long multiplier = 1;
	long long multiple = divisor;

	while (true){
		multiple = multiple * multiplier;
		is_evenly_divisible = least_mulitple(multiple, divisor);
		if (is_evenly_divisible){
			break;
		}
		else{
			multiple += 1;
		}
	}

	cout<<multiple<<endl;
	return 0;
}