def print_list(list_input):
    for each in list_input:
        if isinstance(each, list):
            print "we have a list"
        else
            print "we have a item"


names = ["name", "list", "hello", ["name1", "name2"]]
print_list(names)
