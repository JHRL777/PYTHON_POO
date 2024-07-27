# Clase Automovil
class Automovil:
    def __init__(self, placa, ruedas, color, acientos, estado=True):
        # Inicializa los atributos del automovil
        self.placa = placa
        self.ruedas = ruedas
        self.color = color
        self.acientos = acientos
        self.estado = estado

    def __str__(self):
        # Retorna una cadena de texto que representa el automovil
        return f"""
placa: {self.placa}
Ruedas: {self.ruedas}
Color: {self.color}
Acientos: {self.acientos}
Estado: {self.estado}
----------------------------------
            """

# Clase Carro que hereda de Automovil
class Carro(Automovil):
    def __init__(self, placa, ruedas, color, acientos, marca, modelo):
        # Inicializa los atributos del carro y llama al constructor de Automovil
        super().__init__(placa, ruedas, color, acientos)
        self.marca = marca
        self.modelo = modelo
        self.cantidad = 0

    def __str__(self):
        # Retorna una cadena de texto que representa el carro
        imprimir = f"""
Marca:{self.marca}
Modelo:{self.modelo}
Cantidad:{self.cantidad}
            """ + super().__str__()
        return imprimir

# Clase Motos que hereda de Automovil
class Motos(Automovil):
    def __init__(self, placa, ruedas, color, acientos, marca, modelo, cilindraje):
        # Inicializa los atributos de la moto y llama al constructor de Automovil
        super().__init__(placa, ruedas, color, acientos)
        self.marca = marca
        self.modelo = modelo
        self.cilindraje = cilindraje
        self.cantidad = 0

    def __str__(self):
        # Retorna una cadena de texto que representa la moto
        imprimir = f"""
Marca:{self.marca}
Modelo:{self.modelo}
Cilindraje:{self.cilindraje}
cantidad: {self.cantidad}
            """ + super().__str__()
        return imprimir

# Clase Consesionario
class Consesionario:
    def __init__(self):
        # Inicializa el inventario como una lista vacia
        self.inventario = []

    def agregar_automovil(self, automovil):
        # Agrega un automovil al inventario
        auto_mov = self.buscar(automovil.placa)
        if auto_mov is not None:
            if automovil.marca == auto_mov.marca and automovil.modelo == auto_mov.modelo:
                auto_mov.cantidad += 1
                print(f"Sumado al inventario ya son {auto_mov.cantidad}")
            else:
                automovil.cantidad = 1
                self.inventario.append(automovil)
                print("Agregado con exito")
        else:
            automovil.cantidad = 1
            self.inventario.append(automovil)
            print(f"Agregado con exito {automovil.marca}")

    def ver_automoviles(self):
        # Retorna una lista de todos los automoviles en el inventario
        arra = []
        for automovil in self.inventario:
            arra.append(automovil)
        return arra

    def buscar(self, placa):
        # Busca un automovil en el inventario por su placa
        for automovil in self.inventario:
            if placa == automovil.placa:
                return automovil
        return None

    def venta(self, automovil):
        # Vende un automovil en el inventario
        venta_automovil = self.buscar(automovil)
        if venta_automovil is not None:
            for venta_auto in self.inventario:
                if venta_auto.cantidad <= 1 and automovil == venta_auto.placa:
                    venta_auto.estado = False
                    venta_auto.cantidad -= 1
                    print(f"no quedan mas de este vehiculo")
                elif(automovil == venta_auto.placa):
                    venta_auto.cantidad -= 1
                    print(f"veiculo vendido quedan {venta_auto.cantidad}")
        else:
            print(f"veiculo no exite para la venta placa:{automovil}")

    def actualizar(self, id, obj):
        # Actualiza un automovil en el inventario
        automovilM = self.buscar(id)
        if automovilM is not None:
            for i in range(len(self.inventario)):
                if self.inventario[i].placa == id:
                    if isinstance(obj, Carro) or isinstance(obj, Motos):
                        self.inventario[i] = obj
                    else:
                        print("El objeto debe ser de tipo Carro o Motos")

# Crea un objeto Consesionario
consesionario = Consesionario()

# Agrega automoviles al inventario
carro1 = Carro("bg934", "4", "negro", 5, "Chebrolet", "picanto")
moto1 = Motos("gt77h", 2, "rojo", 2, "kawasaki", "ninja", 900)

consesionario.agregar_automovil(carro1)
consesionario.agregar_automovil(carro1)
consesionario.agregar_automovil(carro1)
consesionario.agregar_automovil(carro1)
consesionario.agregar_automovil(carro1)
consesionario.agregar_automovil(moto1)
consesionario.agregar_automovil(moto1)
consesionario.agregar_automovil(moto1)

# Actualiza un automovil en el inventario
carrom = Carro("bg934", "4", "Rojo", 7, "Chebrolet", "picanto")
consesionario.actualizar("bg934", carrom)

# Menu principal
while True:
    print("""
MENU
          [1] AGREGAR AUTOMOVIL
          [2] VER AUTOMOVILES
          [3] VENTA AUTOMOVIL
          [4] SALIR
""")
    opciones = int(input("marcar la opcion que quieres: "))

    # Agregar automovil
    if opciones == 1:
        print("---------------------------------------------")
        print("AGREGAR AUTO")
        print("---------------------------------------------")
        print("Formulario")
        placa = input("placa de automovil: ")
        ruedas = input("ruedas de automovil: ")
        color = input("color de automovil: ")
        acientos = input("acientos de automovil: ")
        marca = input("marca de automovil: ")
        modelo = input("modelo de automovil: ")

        print("tipo de vehiculo [1]: Carro, [2]Moto")
        tipo = int(input("anade tipo de automovil"))
        if tipo == 1:
            carro = Carro(placa, ruedas, color, acientos, marca, modelo)
            consesionario.agregar_automovil(carro)
        else:
            cilindraje = input("Cilindraje")
            moto = Motos(placa, ruedas, color, acientos, marca, modelo, cilindraje)
            consesionario.agregar_automovil(moto)

    # Ver automoviles
    elif opciones == 2:
        print("---------------------------------------------")
        print("TODOS LOS AUTOMOVILES")
        print("---------------------------------------------")
        allvehculos = consesionario.ver_automoviles()
        for v in allvehculos:
            print(v)

    # Vender automovil
    elif opciones == 3:
        print("---------------------------------------------")
        print("VENDER AUTO")
        print("---------------------------------------------")
        vehculos = consesionario.ver_automoviles()
        for v in vehculos:
            print(f"Placa: {v.placa}  -> modelo: {v.modelo}")
        placa_venta = input("placa de vehiculo a vender: ")
        consesionario.venta(placa_venta)

    # Salir
    elif opciones == 4:
        break