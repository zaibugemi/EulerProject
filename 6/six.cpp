#include <iostream>
using namespace std;

int sum_of_the_squares(int num){
	int square_sum = 0;
	for (int i = 1; i <= num; i++){
		square_sum += i * i;
	}
	return square_sum;
}

int square_of_the_sum(int num){
	int sum = 0;
	for (int i = 1; i <= num; i++){
		sum += i;
	}

	return sum * sum;
}

int main(){

	int number;
	cout<<"Enter the number: ";
	cin>>number;

	cout<<endl<<square_of_the_sum(number) - sum_of_the_squares(number)<<endl;
}