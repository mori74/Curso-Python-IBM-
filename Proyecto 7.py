from os import system
import time

class Persona:
    def __init__(self,nombre,apellidos):
        self.nombre=nombre
        self.apellidos=apellidos

class Cliente(Persona):
    def __init__(self,nombre,apellidos,num_cuenta,balance=0):
        super().__init__(nombre,apellidos)
        self.num_cuenta=num_cuenta
        self.balance=balance

    def __str__(self):
        return f'Bienvenido {self.nombre} {self.apellidos}, su número de cuenta es {self.num_cuenta} y su balance es de {self.balance} €'

    def depositar(self,importe):
        self.balance+=importe
        print(f'Su balance es de {self.balance} €')

    def retirar(self,importe):
        if importe<=self.balance:
            self.balance-=importe
            print(f'Su balance es de {self.balance} €')
        else:
            self.balance=self.balance
            print(f'Su balance es de {self.balance} €')
            print('La cantidad a retirar supera el balance de su cuenta, por favor introduzca otro importe')
dicc_cliente={}
def crear_cliente():
    name=input('Introduzca su nombre: ')
    surname=input('Introduzca sus apellidos: ')
    number_cuenta=input('Introduzca su numero de cuenta: ')
    cliente = Cliente(name, surname, number_cuenta)
    dicc_cliente[cliente.num_cuenta] = cliente
    return cliente

def inicio():

    while True:
        time.sleep(5)
        system('cls')
        print('¿ ES USTED CLIENTE NUEVO ?:\n SI=S\n NO=N')
        respuesta=input('').upper()
        if respuesta=='S':
            client=crear_cliente()

        elif respuesta=='N':
            print('Introduzca su numero de cuenta: ')
            numero_cuenta=input('')
            if dicc_cliente.get(numero_cuenta) is None:
                print('El numero de cuenta introducido no corresponde a ningun cliente')
                continue
            else:
                client=dicc_cliente.get(numero_cuenta)

        while True:
            time.sleep(5)
            system('cls')
            print(client)
            print('¿ QUE OPERACION DESEA REALIZAR ?:\n1= DEPOSITAR (D)\n2= RETIRAR (R)\n3= SALIR (S)')
            operacion = input('').upper()
            if operacion=='D':
                importe = int(input('Introduzca el importe que desea depositar: '))
                client.depositar(importe)

            elif operacion=='R':
                importe = int(input('Introduzca el importe que desea retirar: '))
                client.retirar(importe)
            elif operacion == 'S':
                break
        

inicio()












