import random as r

print(r.random())

print(r.uniform(1,10))

print(r.randint(1,10))

list1 = ["a", "b", "c", "d"]
print(r.choice(list1))
print(r.choices(list1, k = 10))
print(r.sample(list1,k = 3))
list1 = ["a", "b", "c", "d"]
r.shuffle(list1)
print(list1)