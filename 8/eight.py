txtFile = open('eight.txt','r')
txt = txtFile.readlines()
digits = ""

for line in txt:
	digits = digits + line

digits = digits.replace("\n","").replace(" ","")

adj_digits = int(input("Adjacent Digits:"))

largest = 0
sequence = ""
product = 1
for i in range(len(digits) - adj_digits + 1):
	temp = digits[i:i+adj_digits]
	if '0' not in temp:
		for j in range(adj_digits):
			product = product * int(temp[j])
		if product > largest:
			largest = product
			sequence = temp
	product = 1

print("Seq: ", sequence)
print("Val: ", largest)

