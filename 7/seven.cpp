#include <iostream>

int find_nth_prime(int pos);

int main(){

    int pos_input;
    std::cout<<"Enter the desired nth prime number you want:\n";
    std::cin>> pos_input;

    std::cout<<find_nth_prime(pos_input)<<std::endl;
    return 0;
}

int find_nth_prime (int pos) {
    
    int primes_so_far = 0;
    int prime_enumerator = 2;
    int counter;
    
    while (primes_so_far != pos) {
        counter = 0;
        for (int i = 2; i <= prime_enumerator/2; i++){
            if (prime_enumerator % i == 0){ 
                if (++counter != 0) break; //if the counter>0 then the number is composite
            }
        }
        if (counter == 0) primes_so_far++;
        prime_enumerator++;
    }
    return prime_enumerator - 1;
}