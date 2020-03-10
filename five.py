def least_mulitple(num, divisor):
	if divisor == 1:
		return True
	if num % divisor == 0:
		return least_mulitple(num, divisor - 1)
	else:
		return False

divisor = int(input("Enter the number:"))
multiplier = 1
multiple = divisor

while True:
	multiple = multiple * multiplier
	is_evenly_divisible = least_mulitple(multiple, divisor)
	if is_evenly_divisible:
		break
	else:
		multiple += 1

print(multiple)
