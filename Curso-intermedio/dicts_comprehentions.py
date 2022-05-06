def run():
    #my_dict = {}

    #for i in range (1, 101):
    #    if i % 3 != 0:
    #        my_dict[i] = i**3

    my_dict = { i**2 : i**3 for i in range (1, 101) if i % 3 != 0} 
    my_dict_reto = { i : i**0.5 for i in range (1, 1001)}
    odd = list(filter(lambda x: x % 2 != 0, my_dict))


    print(my_dict_reto)
    print(odd)







if __name__== '__main__':
    run()
