def append_size(my_list):
    my_list.append(len(my_list))
    return my_list

my_list = [23, 42, 108]
print(append_size(my_list))
 
def append_sum(my_list):
    for i in range (3):
         my_list.append(my_list[-1] + my_list[-2])
    return my_list
print(append_sum([1, 1, 2]))

def first_three_multiples(num):
    print(num * 1)
    print(num * 2)
    print(num * 3)
    return (num * 3)
print(first_three_multiples(10))

def first_three_multiples(num):
    for i in range (1,4):
        print(num * i)
        return num * 3
    print(first_three_multiples(10))
    