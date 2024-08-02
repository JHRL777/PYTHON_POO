class Producto:

    def __init__(self,id,nombre,descripcion,precio,stock) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock= stock

    def __str__(self) -> str:
        return f"Producto: id: {self.id}\nnombre: {self.nombre}\ndescripcion: {self.descripcion}\nprecio: {self.precio}\nstock: {self.stock}\n___________"
    
    def aumentar_stock(self,aumento):
        self.stock += aumento
    
    def disminuir_stock(self,disminuir):
        self.stock -= disminuir

    


    
class Cliente:

    def __init__(self,id,nombre,email,direccion,telefono) -> None:
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
    
    def __str__(self) -> str:
        return f"Cliente: id: {self.id}\nnombre: {self.nombre}\nemail: {self.email}\ndireccion: {self.direccion}\ntelefono: {self.telefono}\n___________"

class Pedido:

    def __init__(self, id, cliente) -> None:
        self.id = id
        self.cliente = cliente.nombre
        self.productos = []
        self.total = 0
    
    def __str__(self) -> str:
        productos_str = "\n".join([str(producto) for producto in self.productos])
        return f"Pedido: id: {self.id}\nCliente: {self.cliente}\nProductos:\n{productos_str}\nTotal: {self.total}\n___________"


    def pdbuscarid(self,id):
        for producto in self.productos:
            if producto.id == id:
                return producto

    def calcular_total(self):
         self.total = sum(producto.precio for producto in self.productos)
        

    def agregar_producto_pedido(self,id,tienda):
        producto = tienda.pdBuscaId(id)
        if producto is not None:
            self.productos.append(producto)
            self.calcular_total()  # Actualizar el total después de agregar un producto
        else:
            print(f"Producto con ID {id} no encontrado en la tienda.")
        
    def eliminar_producto_eliminar(self,producto):
        self.productos.remove(producto)


class Tienda:

    def __init__(self) -> None:
        self.productos = []
        self.clientes = []
        self.pedidos = []

    def agregar_producto(self,producto):
        self.productos.append(producto)
    
    def eliminar_producto(self,producto):
        self.productos.remove(producto)
    
    def agregar_cliente(self,cliente):
        self.clientes.append(cliente)
    
    def eliminar_cliente(self,cliente):
        self.productos.remove(cliente)
    
    def crear_pedido(self,pedido):
        self.pedidos.append(pedido)
    
    def listar_productos(self):
        for producto in self.productos:
            print(producto)
            
    
    def listar_clientes(self):
        return [str(cliente)for cliente in self.clientes]
             
    
    def listar_pedidos(self):
        for pedido in self.pedidos:
            print(pedido)

    def pdBuscaId(self, id):
        for p in self.productos:
            if p.id == id:
                return p

    def actualizar_producto(self,producto):
        
        for i,p in enumerate(self.productos):
            if p.id == producto.id:
                self.productos[i] = producto
        
    
tienda_eloccidente = Tienda()

produco1 = Producto(1,"Arroz","Arroz huila",2300,100)
produco2 = Producto(2,"Huevos","Huevos campesionos",700,1000)
produco3 = Producto(3,"Carne","Carne Roja de vaca",12000,310)
produco4 = Producto(4,"Sal","Sal de mar",1300,13000)
produco5 = Producto(5,"Alberja","Alberja",2100,1000)
acproducto1 = Producto(2,"Huevosssssssss","Huevos campesionos",900,1000)

cliente1 = Cliente(1,"Jesus santamaria","jesus@cristo.com","Bogota capital",311577745)
cliente2 = Cliente(2,"Sara Hernandez","shernandez@gmil.com","Bogota capital",3115111145)
cliente3 = Cliente(3,"Nicolas Rodriguez","nicor@hotmil.com","Tunja boyaca",311598545)

tienda_eloccidente.agregar_producto(produco1)
tienda_eloccidente.agregar_producto(produco2)
tienda_eloccidente.agregar_producto(produco3)
tienda_eloccidente.agregar_producto(produco4)
tienda_eloccidente.agregar_producto(produco5)
tienda_eloccidente.actualizar_producto(acproducto1)

tienda_eloccidente.agregar_cliente(cliente1)
tienda_eloccidente.agregar_cliente(cliente2)
tienda_eloccidente.agregar_cliente(cliente3)

# Puedes hacer un pedido con los datos indicados
#ejemplo primero inidcialisamos el pedido pedido2 = Pedido(1,Cliente2) y luego ya se llama.
#Recuerde que primero se debe crear el pedido y luego se le pasa a la tienda para alamzanerlo en un lista

pedido1 = Pedido(1,cliente1)
pedido1.agregar_producto_pedido(1,tienda_eloccidente)
pedido1.agregar_producto_pedido(2,tienda_eloccidente)
pedido1.agregar_producto_pedido(4,tienda_eloccidente)

tienda_eloccidente.crear_pedido(pedido1)


print("___________Productos______________")
tienda_eloccidente.listar_productos()

print("___________Clientes______________")

print("\n".join(tienda_eloccidente.listar_clientes()))

print("___________pedido______________")

tienda_eloccidente.listar_pedidos()
