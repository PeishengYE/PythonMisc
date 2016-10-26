""" using recursion call to """
def print_list(list_input):
    for each in list_input:
        if isinstance(each, list):
            print_list(each)
        else:
            print each


names = ["name", "list", "hello", ["name1", "name2"]]
print_list(names)
