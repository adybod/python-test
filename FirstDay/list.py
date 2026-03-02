#data structures

#list
colours = ["purple", "blue", "purple","orange", 1, 3.4, True, "white"]
print(colours[2]) #index number or orange

print(colours[-1]) #negative indexing

print(colours[1:6]) #start:end(exclusive)



#add in a list
colours.append("gray") #adds an extra variable into the list
colours.insert(1,"brown") #adds in specific position

nums = [1,2,3,4,5]
colours.extend(nums)



#removing
colours.remove("brown")


colours.pop(4)
print(colours)


#broadcasting
colours[2]= "green"




#sorting
colours.sort(reverse=True)

colours.reverse()



#tuple - ordered, duplicates are fine, unchangeable, hard coded.
colours = ("purple", "blue", "purple","orange", "orange")
print(colours[-1])

tuple1 = (1,2,4,5,7)
print(tuple1)
list1=list(tuple1)
print(list1)


#dictionaries - key:value pairs
#ordered, no duplicates, mutable

people = {"name":"python","age": 40, "hobby":"writing"}
print(people)

print(people["name"])

people["age"] = 50
print (people)


print(people.get("name")) #will not crash the project
print(people.get("name", "key does not exist")) #will not crash the project

people.update({'name':'java', "age":60})
people.update({"hobby":"reading","country":"india"})
print(people)


people.pop("country")
print(people)

people.popitem()
people.clear() #removes everything
del people #kill the list completely
