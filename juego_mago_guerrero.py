# crear un juego por medio de objetos que va tener uno guerreros mago y guerrerro que se van a enfrentr donde pierde el que quede sin vida primero.
# vamos a craer una classe de personaje donde va tener Nombre,tipo(mago o guerrero),nivel, vida, metodo de decrementar la vida
#class guerrero super(Nombre,tipo(mago o guerrero),nivel), poder
#class mago super(Nombre,tipo(mago o guerrero),nivel), magia
#class arena  una lista de guerreros y magos y metodos de agregar eliminar y batalla

class Personaje:

    TIPOS = ["GUERRERO", "MAGO"]

    def __init__(self,nombre,tipo, nivel, vida) -> None:
        self.nombre = nombre
        if tipo.upper() in Personaje.TIPOS:
            self.tipo = tipo.upper()
        else:
            raise ValueError(f"Tipo inválido. Debe ser uno de {Personaje.TIPOS}.")
        self.nivel = nivel
        self.vida = vida
    
    def atacado(self,ataque):
        self.vida -= ataque
    
    def __str__(self):
        return f"Personaje: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}, Vida: {self.vida}"


class Guerrero(Personaje):

    def __init__(self, nombre, nivel, vida, poder) -> None:
        super().__init__(nombre, Personaje.TIPOS[0], nivel, vida)
        self.poder = poder

    def ataque(self):
        ataque = (self.poder * self.nivel) / 2
        return ataque
    
    def __str__(self) -> str:
        return f"{super().__str__()} poder {self.poder}"

class Mago(Personaje):

    def __init__(self, nombre,nivel, vida,magia) -> None:
        super().__init__(nombre, Personaje.TIPOS[1], nivel, vida)
        self.magia = magia

    def ataque(self):
        magia = (self.magia * self.nivel) / 2
        return magia

    def __str__(self) -> str:
        return f"{super().__str__()} Magia {self.magia}"

class Arena:

    def __init__(self) -> None:
        self.guerreros = []
        self.magos = []

    def agregarGuerrero(self,guerrero):
        self.guerreros.append(guerrero)
    
    def agregarMago(self,mago):
        self.magos.append(mago)
    
    def eliminarGuerrero(self,guerrero):
        self.guerreros.remove(guerrero)
    
    def eliminarMago(self,mago):
        self.magos.remove(mago)

    def mostrarGuerrero(self):
        for guerrero in self.guerreros:
            print(guerrero)

    def mostrarMago(self):
        for mago in self.magos:
            print(mago)

    def buscar(self,tipo,personaje):
        if tipo == "GUERRERO":
            for guerrero in self.guerreros:
                if guerrero.nombre == personaje:
                    return guerrero
        elif tipo == "MAGO":
            for mago in self.magos:
                if mago.nombre == personaje:
                    return mago
        else:
            print(f"No existe ese tipo: {tipo}")
        
  
    
    def batalla(self, tipo_atacante, nombre_atacante, tipo_contrincante, nombre_contrincante):
        atacante = self.buscar(tipo_atacante, nombre_atacante)
        contrincante = self.buscar(tipo_contrincante, nombre_contrincante)
        if atacante and contrincante:
            ataque = atacante.ataque()
            contrincante.atacado(ataque)
            if contrincante.vida < 0:
                if contrincante.tipo == "GUERRERO":
                    print(f"Eliminado guerrero {contrincante.nombre} de tipo {contrincante.tipo}")
                    self.eliminarGuerrero(contrincante)
                elif contrincante.tipo == "MAGO":
                    print(f"Eliminado MAGO  {contrincante.nombre} de tipo {contrincante.tipo}")
                    self.eliminarMago(contrincante)
        else:
            print("Atacante o contrincante no encontrado.")

        
    
arena = Arena()

hercules = Guerrero("Hercules",1,100,15)
aquiles = Guerrero("Aquiles",10,100,32)
thor = Guerrero("thor",2,100,15)

merlin = Mago("merlin",5,100,10)
buldor = Mago("buldor",10,100,30)
poter = Mago("poter",20,100,50)

arena.agregarGuerrero(hercules)
arena.agregarGuerrero(aquiles)
arena.agregarGuerrero(thor)

arena.agregarMago(merlin)
arena.agregarMago(buldor)
arena.agregarMago(poter)

arena.batalla("GUERRERO","Hercules","MAGO","poter")
arena.batalla("MAGO","poter","GUERRERO","Hercules")
arena.batalla("GUERRERO","Aquiles","MAGO","buldor")
arena.batalla("GUERRERO","thor","MAGO","merlin")

print("\n_________OPONETES QUE QUEDAN_____________")
arena.mostrarGuerrero()
print("__________________________")
arena.mostrarMago()

