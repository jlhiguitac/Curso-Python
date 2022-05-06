def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Jorge", "lastname":"Higuita"}
    
    super_list = [
        {"firstname": "Jorge", "lastname":"Higuita"},
        {"firstname": "Vero", "lastname":"Ramírez"},
        {"firstname": "Damaris", "lastname":"Castro"},
        {"firstname": "Celia", "lastname":"Negrita"}
    ]
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,0,1,2],
        "floating_nums": [1.1, 2.2, 3.3]
    }

    for key, value in super_dict.items():
        print(key, "-", value[2])

    for values in super_list:
        for key, value in values.items():
            print(key, "-", value)

    print (super_dict.get("natural_nums"))

if __name__== '__main__':
    run()
