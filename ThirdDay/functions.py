#string methods:

string = "     heLLo  woRld"

print(len(string)) #counts how many charachters in 'string'
print(string.upper()) #all charachters UPPERCASE
print(string.lower()) # all charachters lowercase
print(string.capitalize()) #first letter caps
print(string.title()) #first letter of every word in 'string' as caps
print(string.isupper()) #checks if all charachters are UPPERCASE and gives true or false statement
print(string.islower()) #checks if all charachters are lowercase and gives true or false statement
print(string.istitle()) #checks if first letter of every word in 'string' is caps and gives true or false statement
print(string.isdigit()) #checks if all are numbersand gives true or false statement
print(string.isalpha())
print(string.isalnum())
print(string.replace("heLLo", "hi")) #case sensitive replace
print(string.strip()) #removes unescessary spaces at the start or end
print(string.index("he")) #finds index number
print(string.find("LLo"))


string = "how, are you"
print(string.split()) #splits words and turns it into list
print(string.split(",")) #splits words on specific symbol and turns it into list



list1 = ["how", "are", "you"]
print("add between words".join(list1))

#user defined functions

def greet1():     #defining
    print("good morning")

greet1() #calling




def greet2():
    print(8+1)
    print(9+10)

greet2()

name = "java"

def greet3(name):
    print("good morning", name)

greet3("python") #replaces name. output: "good morning"+"python"

def add(n1,n2):
    print(n1 + n2)

    add(9,10)

