# a = str(input())
#
# list = ["!", ",", ".", "?"]
# i = 0
#
# while i < len(list):
# 	if list[i] in a:
# 		a = a.lower().replace(list[i] , "")
# 		i += 1
# 	else:
# 		i = len(list)
# print(a.lower())

i = 0
s = 0

while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1

print(i)

