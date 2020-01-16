#print the sum of even fibonacci terms not greater than 4000000 i.e. four million
first = 1
second = 1
fib = first + second
total = 0

while fib <= 4000000:
	if fib % 2 == 0:
		total += fib
	first = second
	second = fib
	fib = first + second
print(total)
