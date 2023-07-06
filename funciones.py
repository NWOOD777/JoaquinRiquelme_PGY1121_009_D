import os
import numpy as np
import msvcrt
import time

lista_rut = []

platinum = 120000
gold = 80000
silver = 50000

cantidad = 0
acumulador= 0

escenario = np.zeros((10,10), int)

def cs():
    os.system("cls")


def menu():
    cs()
    print("""\n\tMenú
    
    1. Comprar entradas
    2. Mostrar unicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")

    opcion = validar_opc()
    
    if opcion==1:
        comprar_entradas()
    elif opcion==2:
        mostrar_ubicaciones()
    elif opcion==3:
        ver_listado_asis()
    elif opcion==4:
        mostrar_gan_tot()
    else:
        return
    
def validar_cantidad():
    while True:
        try:
            cant= int(input("Ingrese cantidad de entradas que desea comprar\n -> "))
            if cant >= 0 and cant <= 3:
                return cant
            else:
                print("ERROR! puede comprar un maximo de 3 entradas!")
        except:
            cs()
            print("ERROR! debe ingresar un número entero!")

def comprar_entradas():
    cs()
    
    validar_cantidad()

    mostrar_ubi_dispo()

    seleccionar_ubi()

    validar_rut()

def seleccionar_ubi():
    while True:
        try:
            eleccion = int(input("Ingrese una ubicacion\n -> "))
            if eleccion > 1 and eleccion < 20:
                for x in range[10]:
                        [escenario][x-1] >= 0
                        print("ERROR! esta ubicacion no esta disponible!")
            else:
                for y in range[10]:
                    [escenario][x-1] <= 1
                    print("Gracias por su compra ^_^")
        except:
            cs()
            print("ERROR! debe ingresar un número entero!")

def validar_opc():
    while True:
        try:
            opc = int(input("Ingrese una opción\n -> "))
            if opc in(1,2,3,4,5):
                return opc
            else:
                cs()
                print("ERROR! debe ingresar una opción")
        except:
            cs()
            print("ERROR! debe ingresar un número entero!")

def mostrar_ubicaciones():
    cs()
    for x in range(10):
        print(f"Fila: {x+1}", end=" ")
        for y in range(10):
            print(escenario [x],[y], end=" ")
            print()
    print("Columna: 1 2 3 4 5 6 7 8 9 10")

def validar_rut():
    while True:
        run = input("Ingrese su rut(sin punto ni digito verificador)\n -> ")
        if run > 4000000 and run < 99999999:
            lista_rut.append(run)
            return run
        else:
            print("ERROR! el rut debe tener entr 7 y 8 números")

def mostrar_lista_ruts():
    print(lista_rut.reverse())

def mostrar_ubi_dispo():
    mostrar_ubicaciones()

def ver_listado_asis():
    mostrar_lista_ruts()

def mostrar_gan_tot():
    cs()
    print(f"""
    
    x==========================================x
    |    Tipo entrada   | Cantidad  | Total    |
    x==========================================x
    | Platinum $120.000 | $         | $        |
    x==========================================x
    | Gold     $80.000  | $         | $        |
    x==========================================x
    | Silver   $50.000  | $         | $        |
    x==========================================x
    | Total             | $         | $        |
    x==========================================x
    """)