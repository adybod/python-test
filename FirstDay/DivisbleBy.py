num = int(input("Any random number: "))

ans1 = num % 2
ans2 = num % 3
ans3 = num % 5


if ans1 == 0 :
    var1 = num/2
    print("divisble by 2: ", var1)

if ans2 == 0 :
    var2 = num/3
    print("divisble by 3: ", var2)

if ans3 == 0 :
    var3 = num/5
    print("divisble by 5: ", var3)