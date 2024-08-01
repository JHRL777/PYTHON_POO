class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def __str__(self) -> str:
        return f"PERSONA\nNombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}"

class Empleado(Persona):
    def __init__(self, id, nombre, edad, sexo, cargo):
        super().__init__(nombre, edad, sexo)
        self.cargo = cargo
        self.id = id

    def __str__(self) -> str:
        return f"Empleado\nID: {self.id}\nNombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nCargo: {self.cargo}\n_________________"

class Cliente(Persona):
    def __init__(self, id, nombre, edad, sexo, dinero):
        super().__init__(nombre, edad, sexo)
        self.dinero = dinero
        self.tipoCliente = "Bronze"
        self.id = id

    def __str__(self) -> str:
        return f"Cliente\nID: {self.id}\nNombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nDinero: {self.dinero}\n_________________"

class Cerveza:
    def __init__(self, id, nombre, marca, litros, alcohol, cantidad, precio) -> None:
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.litros = litros
        self.alcohol = alcohol
        self.cantidad = cantidad
        self.precio = precio
        self.estado = "Disponible"
        
    def actualizar_estado(self):
        if self.cantidad == 0:
            self.estado = "Agotado"
    
    def __str__(self) -> str:
        return f"Cerveza\nID: {self.id}\nNombre: {self.nombre}\nMarca: {self.marca}\nCantidad: {self.cantidad}\nPrecio: ${self.precio}\nEstado: {self.estado}\n_______________"

class BarInventario:
    def __init__(self) -> None:
        self.empleados = []
        self.cervezas = []

    def buscarTodoEmpleado(self):
        for empleado in self.empleados:
            print(empleado)
    
    def buscarTodoCerveza(self):
        for cerveza in self.cervezas:
            print(cerveza)
    
    def empleadoID(self, id):
        for empleado in self.empleados:
            if id == empleado.id:
                return empleado
        return None

    def cervezaID(self, id):
        for cerveza in self.cervezas:
            if id == cerveza.id:
                return cerveza
        return None

    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)
    
    def addCerveza(self, cerveza):
        self.cervezas.append(cerveza)
    
    def actualizar_cantidad(self, id, cantidad):
        cerveza = self.cervezaID(id)
        if cerveza:
            cerveza.cantidad -= cantidad
            cerveza.actualizar_estado()
        else:
            print(f"No se encontró la cerveza con ID {id}")

class Venta:
    def __init__(self) -> None:
        self.clientes = []
        self.ventas = []
        self.total = 0
    
    def addcliente(self, cliente):
        self.clientes.append(cliente)

    def buscarCliente(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def buscatodoClientes(self):
        for cliente in self.clientes:
            print(cliente)

    def totalC(self, cerveza, cantidad):
        return cerveza.precio * cantidad

    def fveta(self, idCerveza, barInventario, cantidad, idcliente, idempleado):
        factura = ""
        cerveza = barInventario.cervezaID(idCerveza)
        empleado = barInventario.empleadoID(idempleado)
        cliente = self.buscarCliente(idcliente)
        
        if cerveza and empleado and cliente:
            if cantidad <= cerveza.cantidad:
                total = self.totalC(cerveza, cantidad)
                if total <= cliente.dinero:
                    cliente.dinero -= total
                    barInventario.actualizar_cantidad(idCerveza, cantidad)
                    factura = f"Venta realizada: {cantidad} de {cerveza.nombre} vendida por el empleado {empleado.nombre} al cliente {cliente.nombre} por un total de ${total}."
                    self.ventas.append(factura)
                else:
                    print(f"El cliente {cliente.nombre} no tiene suficiente dinero.")
            else:
                print(f"No hay suficiente cantidad de {cerveza.nombre}. Disponible: {cerveza.cantidad}")
        else:
            print("Empleado, cliente o cerveza no encontrados.")
                
    def verVentas(self):
        for venta in self.ventas:
            print(venta)

bar = BarInventario()
venta = Venta()

cerveza1 = Cerveza(1, "Poker", "Bavaria", 450, 4, 100, 2500)
cerveza2 = Cerveza(2, "Aguila", "Bavaria", 450, 4.5, 110, 2300)
cerveza3 = Cerveza(4, "Andina", "Andina", 450, 4.3, 200, 2100)
cerveza5 = Cerveza(5, "Costeña", "Bavaria", 450, 4.3, 200, 2000)

bar.addCerveza(cerveza1)
bar.addCerveza(cerveza2)
bar.addCerveza(cerveza3)
bar.addCerveza(cerveza5)

empleado1 = Empleado(1, "Maria", 20, "F", "Bartender")
empleado2 = Empleado(2, "Juan", 30, "M", "Administrador")
empleado3 = Empleado(3, "Martin", 27, "M", "Celador")

bar.agregarEmpleado(empleado1)
bar.agregarEmpleado(empleado2)
bar.agregarEmpleado(empleado3)

cliente1 = Cliente(1, "Sergio", 22, "M", 100000)
cliente2 = Cliente(2, "Pablo", 22, "M", 500000)
cliente3 = Cliente(3, "Sandra", 22, "F", 70000)

venta.addcliente(cliente1)
venta.addcliente(cliente2)
venta.addcliente(cliente3)

venta.fveta(1, bar, 2, 1, 1)
venta.fveta(2, bar, 3, 2, 1)

venta.verVentas()

print("-----------------------------------------")
print("-----------------------------------------")
print("-----------------------------------------")
venta.buscatodoClientes()
print("-----------------------------------------")
bar.buscarTodoCerveza()
print("-----------------------------------------")
bar.buscarTodoEmpleado()

            


        