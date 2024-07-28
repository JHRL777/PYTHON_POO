class Libro:
    def __init__(self, titulo, autor, genero, anio_publicacion, estado):
        # Inicializa las propiedades del libro
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.estado = estado

    def __str__(self):
        # Devuelve una representación en cadena del libro
        return f"\n-------\nlibro\n-------\ntitulo: {self.titulo}\nautor: {self.autor}\ngenero: {self.genero}\nanio_publicacion: {self.anio_publicacion}\nestado: {self.estado} "

class Biblioteca:
    def __init__(self, nombre, direccion):
        # Inicializa las propiedades de la biblioteca
        self.nombre = nombre
        self.direccion = direccion
        self.inventario = []
    
    def agregar_libro(self, libro):
        # Agrega un libro al inventario
        self.inventario.append(libro)
    
    def mostrar_inventario(self):
        # Muestra todos los libros en el inventario
        for libro in self.inventario:
            print(libro)
    
    def buscar_libro(self, titulo):
        # Busca un libro por título en el inventario
        for libro in self.inventario:
            if titulo == libro.titulo:
                return libro
        return None
    
    def prestar_libro(self, titulo):
        # Cambia el estado de un libro a 'prestado' si está disponible
        libro = self.buscar_libro(titulo)
        if libro and libro.estado == "disponible":
            libro.estado = "prestado"
            print(f"prestado 🆗\n------------\n{libro}\n---------")
        else:
            print(f"el libro a prestar: {titulo} ya esta prestado ❌")
    
    def devolver_libro(self, titulo):
        # Cambia el estado de un libro a 'disponible' si está prestado
        libro = self.buscar_libro(titulo)
        if libro and libro.estado == "prestado":
            libro.estado = "disponible"
            print(f"se ha devuelto 🆗\n------------\n{libro}\n---------")
        else:
            print(f"no se encuentra titulo a devolver: {titulo} ❌")
    
    def mostrar_libros_prestados(self):
        # Muestra todos los libros que están prestados
        for libro in self.inventario:
            if libro.estado == "prestado":
                print(libro)

# Creación de una instancia de la biblioteca
biblioteca = Biblioteca("Biblioteca centro", "Cartagena")

# Creación de instancias de libros
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 1605, "disponible")
libro2 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", 1954, "disponible")
libro3 = Libro("La Iliada y La Odisea", "Homero", "Poesía", 800, "disponible")
libro4 = Libro("El Principito", "Antoine de Saint-Exupéry", "Cuento", 1943, "disponible")
libro5 = Libro("La Sombra del Viento", "Carlos Ruiz Zafón", "Novela", 2001, "disponible")

# Agregar libros al inventario de la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)

# Pruebas de funcionalidad
biblioteca.prestar_libro("El Principito")
print("----------------------------------------------------------")
biblioteca.devolver_libro("El Principito")
print("----------------------------------------------------------")
biblioteca.prestar_libro("El Principito")
print("----------------------------------------------------------")
biblioteca.prestar_libro("El Principito")
print("------------------LIBROS PRESTADOS-----------------------------------")
biblioteca.mostrar_libros_prestados()
