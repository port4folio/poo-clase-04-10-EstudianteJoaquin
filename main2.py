# from clases.Persona import Persona
# p=Persona("Luis","11.111.111-1")
# print(p.getNombre())
# p.setNombre("Atanasio")
# print(p.imprimir())

# nombre=input("Ingrese nuevo nombre: ")
# p.setNombre(nombre)
# print(p)
# Persona.raza="Cybor"
# p1=Persona("María","22.222.222-2")
# print(p.getNombre(),"es",p.raza)
# print(p1.getNombre(),"es",p1.raza)
# Persona.setRaza("Princesa")
# print(p.getNombre(),"es",p.raza)
# print(p1.getNombre(),"es",p1.raza)

personas=[]

def leer_numero():
    continuar=True
    while continuar:
        try:
            op=int(input())
            continuar=False
        except:
            print("Debe ingresar un número.")
    return op

def menu():
    print("Menu persona")
    print("1.- Agregar")
    print("2.- Editar")
    print("3.- Eliminar")
    print("4.- Imprimir una")
    print("5.- Imprimir todas")
    print("0.- Salir")
    print("Seleccione una opción: ")
    op=leer_numero()
    return op

continuar=True
while continuar:
    op=menu()
    print(f"Ingresó la opción: {op}")
