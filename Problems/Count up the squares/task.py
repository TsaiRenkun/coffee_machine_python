# put your python code here




number = []
num = 0
squareSum = 0

while True:
	num = int(input())
	squareSum = squareSum + (num ** 2)
	number.append(num)
	if sum(number) == 0:
		print(squareSum)
		break




