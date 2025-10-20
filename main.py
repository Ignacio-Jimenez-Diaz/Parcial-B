#Se desea desarrollar un sistema básico para gestionar la participación de atletas en una competición
#deportiva.

class Deportista:
    def __init__(self, nombre, pais, edad, disciplina):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
        self.disciplina = disciplina

    def __str__(self):
        return f" El atleta {self.nombre} de {self.pais} tiene {self.edad} compite en la disciplina {self.disciplina}" 

class Competición:
    def __init__(self):
        self.atletas = []

    def agregar_atleta(self, producto):
        for a in self.atletas:
            if a.codigo == atleta.codigo:
                print(f"error, el atleta {atleta.nombre} ya existe")
                return
    self.atletas.append(atleta)
    print(f"Atleta {atleta.nombre} añadido")

    def eliminar_atleta(self, atleta):
        