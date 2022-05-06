# [1, 1, 2, 2, 4 ] -> my_set = {1, 2, 4}

def remove_duplicates(some_list):
    set_without_duplicates = set()
    for element in some_list:
        set_without_duplicates.add(element)
    return set_without_duplicates

def run():
    ramdom_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(ramdom_list))

if __name__=='__main__':
    run()