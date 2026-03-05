Divby3 = []
Divby5 = []
for i in range(0,51):
    if i % 3==0:
        Divby3.insert(-1,i)
    elif i % 5==0:
        Divby5.insert(-1,i)


print("divisible by 3:", Divby3)
print("divisible by 5:", Divby5)