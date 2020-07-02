# Write your code here


import math

# print("""Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!""")
#

# Part 2
# cups = int(input("Write how many cups of coffee you will need: >"))

# water = 200
# milk = 50
# beans = 15

# print("For " + str(cups)  + " cups of coffee you will need:")
# print(str(cups * water) + "ml of water")
# print(str(cups * milk) + "ml of milk")
# print(str(cups * beans) + "g of beans")

# part 3

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


# part 4 / 5
# water_left = int(input("Write how many ml of water the coffee machine has:> "))
# milk_left = int(input("Write how many ml of milk the coffee machine has:> "))
# beans_left = int(input("Write how many grams of coffee beans the coffee machine has:> "))
# dis_cups = int(input("Write how many disposable cups:> "))
# money = int(input("Write how many much money the coffee machine has:> "))

global water_left
global milk_left
global beans_left
global dis_cups
global money

water_left = 400
milk_left = 540
beans_left = 120
dis_cups = 9
money = 550
keyword = ""

#

while keyword == "":
	choice_input = str(input("Write action(buy, fill, take, remaining, exit): "))

	if(choice_input == "buy"):

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
				3: cappuccino(),
			}
			res = switcher.get(i, "Invalid choice of drink")
			return res

		i = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu: ")

		def is_integer(n):
			try:
				float(n)
			except ValueError:
				return False
			else:
				return float(n).is_integer()

		if(is_integer(i)):
			res = buying_drink(int(i))

			if(water_left < res[0]):
				print("Sorry, not enough water!")
			elif(milk_left < res[1]):
				print("Sorry, not enough milk!")
			elif(beans_left < res[2]):
				print("Sorry, not enough beans!")
			elif(dis_cups == 0):
				print('Sorry, not enough cups!')
			else:

				water_left = water_left - res[0]
				milk_left = milk_left - res[1]
				beans_left = beans_left - res[2]
				dis_cups = dis_cups - 1
				money = money + res[3]


				print("I have enough resources, making you a coffee!")
				print("")

		else:
			continue

	elif(choice_input == "fill"):

		add_water =	int(input("Write how many ml of water do you want to add: "));
		add_milk =	int(input("Write how many ml of milk do you want to add: "));
		add_coffee = int(input("Write how many grams of coffee beans do you want to add: "));
		add_cup =	int(input("Write how many disposable cups of coffee do you want to add: "));
		print("")
		print("The coffee machine has:")

		water_left = water_left + add_water
		milk_left = milk_left + add_milk
		beans_left = beans_left + add_coffee
		dis_cups = dis_cups + add_cup

	elif(choice_input == "take"):

		print("I gave you $" + str(money));

		money = 0

		print("")

	elif(choice_input == "remaining"):

		print("The coffee machine has:")
		print(str(water_left) + " of water")
		print(str(milk_left) + " of milk")
		print(str(beans_left) + " of coffee beans")
		print(str(dis_cups) + " of disposable cups")
		print(str(money) + " of money")
		print("")

	elif(choice_input == "exit"):
		keyword = "exit"
	else:
		print("othering")

