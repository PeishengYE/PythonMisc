def print_lol(input_list):
    for each_list in input_list:
        if isinstance(each_list, list):
            print_lol(each_list)
        else:
            print(each_list)


name = ['name1', 'name2', 'name3',['name2', 'name3', 'name4'] ]
print_lol(name)



