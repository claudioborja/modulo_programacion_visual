'''Cree una clase vacía e instancie un objeto a partir de ella'''
class miclase:
    pass

miclase()

''' Cree una clase con atributos que tengan valores establecidos, retorne dichos atributos, 
instancie un objeto a partir de ella que muestre en pantalla los valores establecidos previamente.'''

class clase_atributos:
    atributo1 = 1
    atributo2 = 2
    atributo3 = 3

    def retornar_atributos(self):
        return self.atributo1, self.atributo2, self.atributo3

objeto = clase_atributos()
print(objeto.retornar_atributos())

'''Cree una clase con atributos que permita que el usuario establezca valores para ellos, 
instancie un objeto a partir de ella que muestre en pantalla los valores establecidos previamente.'''

class clase_atributos_usuario:
    def valores(self, atributo1, atributo2, atributo3):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.atributo3 = atributo3

    def retornar_atributos(self):
        return self.atributo1, self.atributo2, self.atributo3

objeto_dos = clase_atributos_usuario()
objeto_dos.valores(1, 2, 3)
print(objeto_dos.retornar_atributos())

'''Cree una clase con atributos que permita que el usuario establezca valores para ellos, 
instancie un objeto a partir de ella que muestre en pantalla los valores establecidos previamente, 
use el método __init__ para establecer los mismos.'''

class clase_atributos_init:
    def __init__(self, atributo1, atributo2, atributo3):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.atributo3 = atributo3

    def retornar_atributos(self):
        return self.atributo1, self.atributo2, self.atributo3
            
objeto_tres = clase_atributos_init(1, 2, 3)
print(objeto_tres.retornar_atributos())
