# Write your code here


import math

print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")


# Part 2
# cups = int(input("Write how many cups of coffee you will need: >"))

water = 200
milk = 50
beans = 15

# print("For " + str(cups)  + " cups of coffee you will need:")
# print(str(cups * water) + "ml of water")
# print(str(cups * milk) + "ml of milk")
# print(str(cups * beans) + "g of beans")

# part 3
water_left = int(input("Write how many ml of water the coffee machine has:> "))
milk_left = int(input("Write how many ml of milk the coffee machine has:> "))
beans_left = int(input("Write how many grams of coffee beans the coffee machine has:> "))
# # milk_left = int(input("Write how many ml of milk the coffee machine has:> "))
# # beans_left = int(input("Write how many grams of coffee beans the coffee machine has:> "))
# cups_needed = int(input("Write how many cups of coffee you will need:> "))
#
# able_water = math.floor(water_left / water)
# able_milk = math.floor(milk_left / milk)
# able_beans = math.floor(beans_left / beans)

# list = [able_beans, able_water, able_milk]

# if min(list) == cups_needed:
# 	print("Yes, I can make that amount of coffee")
# elif min(list) > cups_needed:
# 	print ("Yes, I can make that amount of coffee", "(and even " + str(min(list) - cups_needed) + " more than that)" )
# elif min(list) < cups_needed:
# 	print ("No, I can make only " + str(min(list)) + " cups of coffee")


# part 4

dis_cups = int(input("Write how many disposable cups:> "))
money = int(input("Write how many much money the coffee machine has:> "))


print("The coffee machine has:")
print(str(water_left) + " of water")
print(str(milk_left) + " of milk")
print(str(beans_left) + " of coffee beans")
print(str(dis_cups) + " of disposable cups")
print(str(money) + " of money")

choice_input = str(input("Write action(buy, fill, take): > "))

if(choice_input == "buy"):
	print("buying")

	def espresso():
		water_needed = 250
		milk_needed = 0
		coffee_needed = 16
		cost = 4
		return water_needed,milk_needed,coffee_needed,cost

	def latte():
		water_needed = 350
		milk_needed = 75
		coffee_needed = 20
		cost = 7
		return water_needed,milk_needed,coffee_needed,cost


	def cappuccino():
		water_needed = 200
		milk_needed = 100
		coffee_needed = 12
		cost = 6
		return water_needed, milk_needed, coffee_needed,cost

	def buying_drink(i):
		switcher = {
			1: espresso(),
			2: latte(),
			3: cappuccino()
		}
		res = switcher.get(i, "Invalid choice of drink")
		return res

	res = buying_drink(int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: > ")))

	print("The coffee machine has:")
	print(res)
	print(str(water_left - res[0]) + " of water")
	print(str(milk_left - res[1]) + " of milk")
	print(str(beans_left - res[2]) + " of coffee beans")
	print(str(dis_cups - 1) + " of disposable cups")
	print(str(money + res[3]) + " of money")

elif(choice_input == "fill"):


	add_water =	int(input("Write how many ml of water do you want to add: > "));
	add_milk =	int(input("Write how many ml of milk do you want to add: > "));
	add_coffee = int(input("Write how many grams of coffee beans do you want to add: > "));
	add_cup =	int(input("Write how many disposable cups of coffee do you want to add: > "));

	print("The coffee machine has:")
	print(str(water_left + add_water) + " of water")
	print(str(milk_left + add_milk) + " of milk")
	print(str(beans_left + add_coffee) + " of coffee beans")
	print(str(dis_cups + add_cup) + " of disposable cups")
	print(str(money) + " of money")

elif(choice_input == "take"):
	print("taking")

	print("I gave you $" + str(money));

	money = 0

	print("The coffee machine has:")
	print(str(water_left) + " of water")
	print(str(milk_left) + " of milk")
	print(str(beans_left) + " of coffee beans")
	print(str(dis_cups) + " of disposable cups")
	print(str(money) + " of money")
else:
	print("othering")

