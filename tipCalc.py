dinnerCost = input("How much was your bill? ")
tipPercentage = input("What percentage would you like to tip? Include the decimal point. ")
totalDinnerCost = dinnerCost + (dinnerCost * tipPercentage)

message = "Your dinner, tip included, costs: {0}".format(totalDinnerCost)

print(message)
