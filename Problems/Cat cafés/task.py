
name = input()
cafe = []
while name != "MEOW":
    cafe += name.split()
    name = input()

largest_index = 1
for i in range(1, len(cafe), 2):
    cafe[i] = int(cafe[i])
    if cafe[i] > cafe[largest_index]:
        largest_index = i

print(cafe[largest_index - 1])