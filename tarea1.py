
from datetime import datetime

today = datetime.now()
f = open("Registros.txt", "w")
pila = []
ciclo = ""
string_today = today.strftime("%m/%d/%Y, %H:%M:%S")

while (True):
    inxx = 0
    print("\n"+"----------Estado actual de la pila--------------------------")
    if (pila == []): print("Vacia")
    else:
        for x in pila:
            print("[","(",inxx + 1,")", x, "]",  end="")
            inxx += 1
    inxx = 0
    print("\n"+"Escribe 1 para almacenar caracteres en la pila"+"\n"+"Escribe 2 para comparar pilas")
    opcion = input()
    f.write(string_today+ " Menu de accion: Ingreso del usuario'"+ opcion+ "'"+"\n")
    if (opcion == "1"):
        while (True):
            print("Ïngresa el caracter a agregar a la pila"+"\n"+"   Si no quieres agregar mas escribe 'exit' "+"\n")
            caracter = input()
            if (caracter == "exit"):
                f.write(string_today+ " Caracter a pila: Ingreso del usuario'"+ caracter+ "'"+"\n")
                if (ciclo == ""):
                    break
                pila.append(ciclo)
                f.write(string_today+ " Caracter a pila: Se añade cadena '"+ciclo+ "' a la pila"+"\n")
                ciclo = ""
                break
            elif (len(caracter) == 1):
                f.write(string_today+ " Caracter a pila: Ingreso del usuario'"+ caracter+ "'"+"\n")
                ciclo += caracter
            else:
                f.write(string_today+ " Caracter a pila: Ingreso del usuario'"+ opcion+ "' Error"+"\n")
                print("Ingresa solamente un caracter")
        continue
    elif (opcion == "2"):
        while (True):
            try:
                print("Ingresa los indices de las cadenas comparar separados con un espacio")
                a, b = input().split(" ")
                f.write(string_today+ " Comparar pilas: Ingreso del usuario'"+ caracter+ "'"+"\n")
                if (pila[int(a)-1] == pila[int(b)-1]):
                    f.write(string_today+ " Caracter a pila: Las cadenas son identicas"+"\n")
                    print("Las cadenas son identicas")
                else: 
                    print("Las cadenas no coiciden")
                    f.write(string_today+ "Caracter a pila: Las cadenas son identicas"+"\n")
            except:
                f.write(string_today+ "Caracter a pila: Error"+"\n")
                print("Ejemplo: '1 2' para comparar la primera y la segunda cola")
            finally:
                break
    else: 
        f.write(string_today+ "Menu de accion: Ingreso del usuario'"+ opcion+ "'"+ "Error"+"\n")
        print("Ingresa una opcion valida"+"\n"+"\n")
                
        
    
    

