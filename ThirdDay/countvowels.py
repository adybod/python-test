def count_vowels(text):
    count=0
    for i in text:
        if i == "e" or i == "o":
            count +=1
    print(count)
    
count_vowels("hello")


