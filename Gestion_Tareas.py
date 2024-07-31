class Tarea:
    def __init__(self, id, nombre, descripcion):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__estado = "Activo"

    def __str__(self) -> str:
        return f"Nombre tarea: {self.__nombre}\nDescripción: {self.__descripcion}\nEstado: {self.__estado}\n____________________"

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

class GestorDeTareas:
    def __init__(self):
        self.listaTareas = []

    def buscarTodo(self):
        return [str(tarea) for tarea in self.listaTareas]

    def agregar(self, tarea):
        self.listaTareas.append(tarea)

    def buscarid(self, id):
        for tarea in self.listaTareas:
            if tarea.id == id:
                return tarea
        return None

    def eliminar(self, id):
        tarea = self.buscarid(id)
        if tarea:
            self.listaTareas.remove(tarea)

    def estado(self, id):
        tarea = self.buscarid(id)
        if tarea and tarea.estado != "Completado":
            tarea.estado = "Completado"

# Ejemplo de uso:
gestorDeTareas = GestorDeTareas()

tarea1 = Tarea(1, "Java", "Aprender Java")
tarea2 = Tarea(2, "MYSQL", "Aprender MYSQL")
tarea3 = Tarea(3, "Python", "Aprender Python")

gestorDeTareas.agregar(tarea1)
gestorDeTareas.agregar(tarea2)
gestorDeTareas.agregar(tarea3)

print(gestorDeTareas.buscarid(1))
gestorDeTareas.estado(2)
print("\n".join(gestorDeTareas.buscarTodo()))
print("__________________________")
gestorDeTareas.eliminar(3)



    
        