# A program to sort my_list in ascending order.

def generate_list(some_list):
    some_list = [81, 57, 30, 43, 72, 99, 18, 33, 4, 50]

def sort_list(some_list):
    for i in range(len(some_list)):
        for j in range(len(some_list) - i):
            if some_list[j] < some_list[j+1]:
                some_list[j], some_list[j+1] = some_list[j+1], some_list[j]

# No bugs in this function
def validate_list(some_list):
    return some_list == sorted(some_list)


my_list = []
generate_list(my_list)
sort_list(my_list)
print(my_list)

if validate_list(my_list):
    print("List sorted successfully.")
else:
    print("Something's wrong.")


