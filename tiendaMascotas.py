# Clase que representa una mascota
class Mascota:

    # Constructor de la clase Mascota
    def __init__(self, nombre, edad, tipo, raza):
        """
        Inicializa una nueva mascota con los parámetros proporcionados.

        Args:
            nombre (str): Nombre de la mascota
            edad (int): Edad de la mascota
            tipo (str): Tipo de mascota (perro, gato, etc.)
            raza (str): Raza de la mascota
        """
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.raza = raza

    # Método que devuelve una representación en cadena de la mascota
    def __str__(self):
        """
        Devuelve una cadena con la información de la mascota.

        Returns:
            str: Información de la mascota
        """
        return f"Mascota: {self.nombre}\nTipo: {self.tipo}\nEdad: {self.edad}\nRaza: {self.raza}"


# Clase que representa una tienda de mascotas
class TiendaMascotas:

    # Constructor de la clase TiendaMascotas
    def __init__(self, nombre, direccion):
        """
        Inicializa una nueva tienda de mascotas con los parámetros proporcionados.

        Args:
            nombre (str): Nombre de la tienda
            direccion (str): Dirección de la tienda
        """
        self.nombre = nombre
        self.direccion = direccion
        self.inventario = []

    # Método que agrega una mascota al inventario
    def agregar_mascota(self, mascota):
        """
        Agrega una mascota al inventario si no está ya presente.

        Args:
            mascota (Mascota): Mascota a agregar
        """
        if mascota not in self.inventario:
            self.inventario.append(mascota)
            print(f"Mascota {mascota.nombre} agregada al inventario")
        else:
            print(f"Mascota {mascota.nombre} ya está en el inventario")

    # Método que muestra el inventario de mascotas
    def mostrar_inventario(self):
        """
        Muestra el inventario de mascotas de la tienda.
        """
        print(f"Inventario de {self.nombre}:")
        for mascota in self.inventario:
            print(mascota)

    # Método que busca una mascota por nombre
    def buscar_mascota(self, nombre):
        """
        Busca una mascota por nombre en el inventario.

        Args:
            nombre (str): Nombre de la mascota a buscar

        Returns:
            Mascota: Mascota encontrada o None si no se encuentra
        """
        for mascota in self.inventario:
            if nombre == mascota.nombre:
                return mascota
        return None

    # Método que vende una mascota
    def vender_mascota(self, nombre):
        """
        Vende una mascota si está presente en el inventario.

        Args:
            nombre (str): Nombre de la mascota a vender
        """
        mascota = self.buscar_mascota(nombre)
        if mascota:
            self.inventario.remove(mascota)
            print(f"Mascota {mascota.nombre} vendida")
            self.mostrar_inventario()
        else:
            print(f"Mascota {nombre} no encontrada en el inventario")


# Creación de objetos y llamadas a métodos
tienda1 = TiendaMascotas("Mascotas Prime", "Bogota")

mascota1 = Mascota("Pepito", 1, "perro", "doberman")
mascota2 = Mascota("Princes", 2, "gato", "siames")
mascota3 = Mascota("firulaiz", 3, "perro", "bloudog")
mascota4 = Mascota("juanito", 4, "gato", "Gato persa")
mascota5 = Mascota("Pepito", 5, "perro", "salchica")

tienda1.agregar_mascota(mascota1)
tienda1.agregar_mascota(mascota2)
tienda1.agregar_mascota(mascota3)
tienda1.agregar_mascota(mascota4)
tienda1.agregar_mascota(mascota5)

tienda1.mostrar_inventario()

tienda1.buscar_mascota("Pepito")

tienda1.vender_mascota("Pepito")
