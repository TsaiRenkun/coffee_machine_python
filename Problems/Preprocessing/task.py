a = str(input())

list = ["!", ",", ".", "?"]
i = 0

while i < len(list):
	if list[i] in a:
		a = a.lower().replace(list[i] , "")
		i += 1
	else:
		i = len(list)
print(a.lower())