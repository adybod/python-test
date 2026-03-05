#palindrome
n = 123
reverse = ""

for i in range (1,4):
    remainder = n % 10
    remainder = str(remainder)
    reverse = reverse +remainder
    n = n // 10
    remainder = int(remainder)

print("rev",reverse)

# continue skips,
# break stops
# pass