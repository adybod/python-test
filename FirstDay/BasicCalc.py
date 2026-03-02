num1 = int(input("first number: "))
method = input("method: ")
num2 = int(input("second number: "))

if "Multiply" in method:
   val1 = num1 * num2
   print(val1)
elif "Add" in method:
   val2 = num1 + num2
   print(val2)
elif "Subtract" in method:
   val3 = num1 - num2 
   print(val3)
elif "Divide" in method:
   val4 = num1 / num2
   print(val4)