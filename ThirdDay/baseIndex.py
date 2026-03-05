def add():
    n1 = int(input(""))
    n2 = int(input(""))

    print(n1 ** n2)

add()

#or

def add():
    print(n1 ** n2)

n1 = int(input(""))
n2 = int(input(""))
add()


#positional arguments
def test(name,age,city):
    print("name:",name,"age:",age,"city:",city)
test("python",50,"mumbai")


test(city = "Mumbai", name = "python", age = 50) #keyword arguments

def area(r, pi = 3.14):
    print(r * r * pi)

area(5) #=78.5
area(3,4.5)

def test(*args):
    print(args)

test(1,2,3,4,5,"hi")





args = (4,5,6,7,8)
sum = 0

for i in args:
    sum = sum + 1
print(sum)




def total(*args):
    sum = 0
    for i in args:
        sum = sum + i 
    print (sum)
total(5,6,7,2,0)