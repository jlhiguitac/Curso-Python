def make_division(x):
    def division(n):
        assert x != 0, "No se puede dividir por cero"
        return n/x
    return division

division_by_3 = make_division(3)
print(division_by_3(18))
division_by_5 = make_division(5)
print(division_by_5(100))
division_by_1 = make_division(1)
print(division_by_1(100))