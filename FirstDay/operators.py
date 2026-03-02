#operators

a = 10
b = 20

print(a + b) #addition - sum of a and b
print(a - b) #subtraction - difference of a and b
print(a * b) #multiplication - product of a and b
print(a / b) #division - quotient of a and b
print(a % b) #modulus - remainder of the division of a and b
print(a ** b) #exponentiation - a to the power of b
print(a // b) #floor division - integer division of a and b


#comparison operators
print(a == b) #equal to
print(a != b) #not equal to
print(a > b) #greater than
print(a < b) #less than
print(a >= b) #greater than or equal to
print(a <= b) #less than or equal to

a = 10
b = 3
c = 7

print(a > b and a > c) #expects all conditions to be true
print(a > b or a > c) #at least one condition has to be true
print(not (a > b)) #opposite of condition


#membership operators

string = 'hello'
print("e" in string) #true if e is in string
print("p" not in string) #true if p is not in string


#assignment operators
x = 9
print(x)
x += 2 #x = x + 2 = 9 + 2 = 11
print(x)
x -= 3 #x = x - 3...
print(x)
x *= 3
x /= 3
x //= 3
x %= 3
x **= 3 


#identity operators
string1 = "hello"
string2 = "Hello"

print(string1 is string2)
print(string1 is not string2)



