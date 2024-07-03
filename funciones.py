import os, time, csv

registros:[]
cil_5kg: 12.500
cil_15kg: 25.500


def menu():
    while True:
     os.system('cls')
     print("---BIENVENIDO A GAXPLOSIVE---")
     print("1. Registrar Pedido")
     print("2. Listar todos los pedidos")
     print("3. Buscar pedido por RUT")
     print("4. Imprimir hoja de ruta.")
     print("5. Salir")
    
     opc = int(input("SELECCIONE UNA OPCIÓN: "))
     if opc==1:
         os.system('cls')
         print("---Registrar Pedido---")
         time.sleep(1.5)
         os.system('cls')
         while True:
          rut=input("Ingrese su RUT: ")
          if len(rut)>3:
            print("Rut Ingresado Con Exito!")
            
            pass
          elif len(rut)<3:
            print("ERROR! DEBES INGRESAR UN RUT CON 9 CARACTERES")
            return
          while True:
             nombre=input("Ingrese Su Nombre: ")
             print("Nombre Ingresado Con Exito!")
             time.sleep(0.5)
             direccion=input("Ingrese Su Dirección: ")
             comuna=input("Ingrese Su Comuna: ")
             print("Dirección y Comuna Ingresadas Con Exito!")
             time.sleep(0.5)
             detalles=input("¿Desea Detallar Algo En Su Direccion?: ")
             os.system('cls')
             print("Información Del Comprador Ingresada Con Exito!!")
             time.sleep(2)
             os.system('cls')
             while True:
              cil = int(input("Seleccione El Galon Que Desea Llevar (5KG: $12.500 15KG: $25.500): "))
              if cil==5:
                 print("Galon Selecciónado: 5KG")
                 cantidad_cil_5=int(input("¿Cuantos Cilindros de 5KG Desea?: "))
              elif cil==15: 
                 print("Galon Selecciónado: 15KG") 
                 cantidad_cil_15=int(input("¿Cuantos Cilindros de 15KG Desea?: "))

            
     elif opc==2:
        listar_pedidos: ()
     elif opc==3:
        if len(registros)==0:
           print("El Historial Esta Vacio! Añade Un Registro Antes!(Opcion 1)")
     elif opc==4:
        imprimir_hr: ()
     elif opc==5:
        print("ADIOS! GRACIAS POR CONFIAR EN NOSOTROS!!")
        exit()
     else: 
       print("ERROR! OPCIÓN INCORRECTA!")
       time.sleep(3)