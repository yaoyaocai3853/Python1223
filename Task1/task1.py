main = input("How many main courses would you like?")
dessert = input("How many desserts would you like?")
drinks = input("How many drinks would you like?")

main = float(main)
drinks = float(drinks)
dessert = float(dessert)

mainCost = main * 12.50
dessertCost = dessert * 6
drinkCost = drinks * 3.55
totalCost = drinkCost + dessertCost + mainCost

print(f"{main} mains at 12.5 is {mainCost}")
print(f"{dessert} desserts at 6 is {dessertCost}")
print(f"{drinks} drinks at 3.55 is {drinkCost}")
print(f"Total price of meal is ${totalCost}")