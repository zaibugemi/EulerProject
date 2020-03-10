# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

number = int(input("Enter the number:"))
iterator = 2

def find_prime(number, to_be_factor):
	while True:
		if number % to_be_factor == 0:
			return to_be_factor
		else:
			to_be_factor += 1

counter = 0
def is_prime(number):
	if number == 1 or number == 0:
		return 0
	if number % iterator == 0:
		counter += 1
		number = number / a_factor
	else:
		iterator += 1
		return is_prime(number)


prime_factors_list = []
prime_factors_set = set()

while True:
	if number == 1:
		break
	else:
		a_factor = find_prime(number, iterator)
		prime_factors_list.append(a_factor)
		prime_factors_set.add(a_factor)
		number = number / a_factor
		
print(prime_factors_list)
print(prime_factors_set)

