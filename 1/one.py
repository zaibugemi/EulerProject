#find the sum of numbers smaller than 1000 that are multiples of 3 or 5

total = 0
for i in range(1,1000):
	if (i % 3 == 0) or (i % 5 == 0):
		total += i
print(total)