# Write your code here
print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")

cups = int(input("Write how many cups of coffee you will need: >"))

water = 200
milk = 50
beans = 15

print("For " + str(cups)  + " cups of coffee you will need:")
print(str(cups * water) + "ml of water")
print(str(cups * milk) + "ml of milk")
print(str(cups * beans) + "g of beans")