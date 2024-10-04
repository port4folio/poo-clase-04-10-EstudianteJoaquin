class Persona:
    raza="Humano"
    def __init__(self,nombre,rut):
        self.__nombre=nombre
        self.__rut=rut
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getRut(self):
        return self.__rut
    def setRut(self,rut):
        self.__rut=rut
    def imprimir(self):
        return f"Nombre: {self.__nombre}\nR.U.N. {self.__rut}"
    def __str__(self):
        return f"Nombre: {self.__nombre}\nR.U.N. {self.__rut}"
    
    @classmethod
    def setRaza(cls,raza):
        cls.raza=raza