def list1(new_list):
    value = new_list[0]
    for i in new_list:
        if (i > value):
            value = i
    print(value)

list1([1,2,4,6])