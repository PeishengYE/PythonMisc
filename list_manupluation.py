cmd_mutt = ["mutt",  "-s", "Motion detected ", "peisheng.ye.88@gmail.com", "-a"] 

def add_list(files):
    all_list = cmd_mutt + files
    return all_list
     

files = ["hello1", "hello2","hello3", "hello4"]
final_files = add_list(files)

for each in final_files:
    print(each)


