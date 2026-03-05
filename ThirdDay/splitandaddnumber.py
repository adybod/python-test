def n1(n):
    reverse = 0
    for i in range (1,4):
        number = n % 10
        reverse = reverse + number
        n = n // 10
    print("rev", reverse )
    
n1(123)
