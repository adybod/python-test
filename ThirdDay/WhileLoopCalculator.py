
while True:
    choice = input("method: ")
    if choice == "quit":
        break

    n = int(input("1st number: "))
    n1 = int(input("2nd number: "))



    if (choice == "add"):
        print(n, "+", n1, "=", n+n1)
    elif (choice == "subtract"):
        print(n, "-", n1, "=", n-n1)
    elif (choice == "multiply"):
        print(n, "x", n1, "=", n*n1)
    elif (choice == "divide"):
        print(n, "%", n1, "=", n/n1)

# while True:
#     user_input=input("Input:")
#     if user_input == "quit":
#      break