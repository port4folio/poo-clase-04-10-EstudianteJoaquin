# from clases.Persona import Persona
# p=Persona("Luis","11.111.111-1")
# print(p.getNombre())
# p.setNombre("Atanasio")
# print(p.imprimir())

# nombre:Luis
# p.setNombre(nombre)
# print(p)
# Persona.raza="Cybor"
# p1=Persona("María","22.222.222-2")
# print(p.getNombre(),"es",p.raza)
# print(p1.getNombre(),"es",p1.raza)
# Persona.setRaza("Princesa")
# print(p.getNombre(),"es",p.raza)
# print(p1.getNombre(),"es",p1.raza)

from clases.Persona import Persona
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

def AgregarPersona():
    nombre=input("Ingrese nombre: ")
    rut=input("Ingrese rut: ")
    persona=Persona(nombre, rut)
    persona.append(persona)

def ImprimirPersonas():
    for persona in personas:
        print("***********")
        print(persona)

def buscar_persona():
    rut=input("Ingrese rut a buscar: ")
    for persona in personas:
        if persona.getRun()==rut:
            return persona
        return None 

def EditarPersona():
    persona=buscar_persona()
    if persona!=None:
        print(f"Su nombre actual es {persona.getNombre()}")
        nombre=input("Ingrese nuevo nombre.")
        if nombre=="":
            print("no se realizon cambios.")
        persona.setNombre(nombre)
    else:
        print("Persona no encontrada")
def EliminarPersona():
    persona=buscar_persona()
    if persona!=None:
        personas.remove(persona)
    else:
        print("Persona no encontrada.")

def ImprimirPersona():
    persona=buscar_persona()
    if persona!=None:
        personas.remove(persona)#el objeto dentro de un print llama al_str_()
    else:
        print("Persona no encontrada.")


continuar=True
while continuar:
    op=menu()
    if op==1:
      AgregarPersona()
    elif op==2:
      EditarPersona()
    elif op==3:
        EliminarPersona()
    elif op==4:
     ImprimirPersona()
    elif op==5:
     ImprimirPersonas()
    elif op==0:
        print("¡¡Gracias!!")
        continuar=False