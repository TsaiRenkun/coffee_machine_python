import math
print("working")

def dynamic(pi, Qtyi):
#  pi also represents the parent node.
# 	pi will be an object with itemID, stocks, Qty

	stocks = math.floor(int(pi.stock)/int(Qtyi))
	return stocks

def fixed(pi,Qtyi,Si):
	stock_fixed=(int(Qtyi) * int(Si))
	return stock_fixed

item_array = []

class nodes:
	def __init__(self,choice,parent,Qtyi,Si,item,stock):
		self.choice = choice
		self.parent = parent
		self.Qtyi = Qtyi
		self.Si = Si
		self.item = item
		self.stock = stock

class FirstInput:
		def __init__(self,item,stock):
				self.item = item
				self.stock = stock

N, M = input("Enter 2 values: > ").split()

First = FirstInput(N,M)

print(First.item, "number of Items")
print(First.stock, "number of stocks")

item_array.append(First)

print(item_array[0].item)

i = 0
while i < int(First.item):

	choice, pi, Qtyi, *Si = input().split()
	if int(choice) == 1:

			# Dynamic Choice
			node_Dynamic = nodes(choice, pi, Qtyi, Si, int(pi)+1, 0)

			# Helper function
			stocks = dynamic(item_array[int(pi)-1],Qtyi)
			node_Dynamic.stock = stocks

			# Append new node to item_array
			item_array.append(node_Dynamic)
			i += 1
	elif int(choice) == 2:

		# fixed Choice
		node_fixed = nodes(choice, pi, Qtyi, int(Si[0]), int(pi) + 1, 0)

		# Helper function
		stocks = fixed(item_array[int(pi) - 1], Qtyi, int(Si[0]))
		node_fixed.stock = stocks

		# Append new node to item_array
		item_array.append(node_fixed)
		i += 1
	else:
		print("Wrong choice")
