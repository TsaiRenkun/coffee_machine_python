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
cups_needed = int(input("Write how many cups of coffee you will need:> "))

able_water = math.floor(water_left / water)
able_milk = math.floor(milk_left / milk)
able_beans = math.floor(beans_left / beans)

list = [able_beans, able_water, able_milk]

if min(list) == cups_needed:
	print("Yes, I can make that amount of coffee")
elif min(list) > cups_needed:
	print ("Yes, I can make that amount of coffee", "(and even " + str(min(list) - cups_needed) + " more than that)" )
elif min(list) < cups_needed:
	print ("No, I can make only " + str(min(list)) + " cups of coffee")


