print("Welcome to 'Two Numbers.' We will ask you for two numbers and tell you their sum." )

num1 = raw_input("Enter the first number: ")
num2 = raw_input("Enter the second number: ")

sumNums = (int(num1,10) + int(num2,10))

message = "Their sum equals {0}.".format(sumNums)

print(message)
