class Pajaro:

    alas= True

    def __init__(self,color,especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print(f'pío, mi color es {self.color}')

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')

piolin=Pajaro('amarillo','canario')

piolin.piar()