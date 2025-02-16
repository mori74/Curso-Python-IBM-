class Animal:

    def __init__(self,edad,color):
        self.edad=edad
        self.color=color

    def nacer(self):
        print('este animal ha nacido')

    def hablar(self):
        print('este animal emite un sonido')

class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo=altura_vuelo

    def hablar(self):
        print('pio')
    def volar(self,metros):
        print(f'el pajaro vuela {metros} metros')

piolin=Pajaro(3,'amarillo',60)
piolin.hablar()
piolin.volar(100)

class Padre():
    def hablar(self):
        print('hola')
class Madre():
    def reir(self):
        print('jajajjaa')
    def hablar(self):
        print('que tal')
class Hijo(Madre,Padre):
    pass
class Nieto(Hijo):
    pass

mi_nieto=Nieto()
mi_nieto.reir()
mi_nieto.hablar()
mi_hijo=Hijo()
mi_hijo.hablar()

print(Nieto.__mro__)

print(object.__doc__)