# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome():
	number = 0
	largest_palin = (0,0,0)
	
	for i in range(100,1000):
		for j in range(100,1000):
			number = i * j
			num_str = str(number)
			len_half = int(len(num_str)/2)
			reverse_str = num_str[::-1]
			if len(num_str) % 2 == 0:
				if num_str[0:len_half] == reverse_str[0:len_half] and number > largest_palin[0]:
					largest_palin = (number,i,j)
			else:
				if num_str[0:len_half] == reverse_str[0:len_half] and number > largest_palin[0]:
					largest_palin = (number,i,j)

	print("Largest palindrome from the product of two 3-digit numbers:{}, {} * {}".format(largest_palin[0],largest_palin[1],largest_palin[2]))

palindrome()