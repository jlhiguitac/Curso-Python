import time

class FiboIter:
    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration

if __name__=='__main__':
    max = int(input("Ingresa el el número máximo de elementos de la serie que quieres..."))
    assert  type(max) == int, "debes ingresar un número entero"
    fibonacci = FiboIter(int(max))
    for element in fibonacci:
        print (element)
        time.sleep(0.3)