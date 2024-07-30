# Clase Empleado para representar un empleado con nombre, apellido, cargo y salario
class Empleado:
    def __init__(self, nombre, apellido, cargo, salario):
        # Inicializa los atributos del empleado
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.salario = salario

    # Método para calcular el salario neto (salario - 20% de pretaciones)
    def salarioNeto(self):
        pretaciones = self.salario * 0.2
        salarioNeto = self.salario - pretaciones
        return salarioNeto

    # Método para representar el empleado como un string
    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.cargo}, Salario: {self.salario}, Salario Neto: {self.salarioNeto()}"

# Clase Departamento para representar un departamento con nombre y lista de empleados
class Departamento:
    def __init__(self, nombre):
        # Inicializa el nombre del departamento y la lista de empleados
        self.nombre = nombre
        self.lista = []

    # Método para agregar un empleado al departamento
    def agregar(self, empleado):
        self.lista.append(empleado)

    # Método para mostrar la lista de empleados del departamento
    def mostrar_lista(self):
        print(f"Lista de departamentos: {self.nombre}")
        for empleado in self.lista:
            print(empleado)

# Crea departamentos y empleados
departamento = Departamento("Tecnologia")
departamento1 = Departamento("Administrativo")

empleado1 = Empleado("Nicolas", "Martines", "Ingeniero", 5400000)
empleado3 = Empleado("Juan", "Reyes", "Tecnico", 2400000)
empleado2 = Empleado("Maria", "Reyes", "Desarrollador", 3400000)

empleado4 = Empleado("Sofia", "Martines", "Contador", 2400000)
empleado5 = Empleado("Juan", "Reyes", "Administrador", 3400000)
empleado6 = Empleado("Maria", "Reyes", "Auxiliar administrativa", 1400000)

# Agrega empleados a los departamentos
departamento.agregar(empleado1)
departamento.agregar(empleado3)
departamento.agregar(empleado2)

departamento1.agregar(empleado4)
departamento1.agregar(empleado5)
departamento1.agregar(empleado6)

# Muestra la lista de empleados de cada departamento
print("---------------------------------")
departamento.mostrar_lista()
print("---------------------------------")
departamento1.mostrar_lista()
print("---------------------------------")
