import math

# objeto donde se solicita los numeros
class Numeros:

    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def __str__(self) -> str:
        return f"Numero 1: {self.num1}\nNumero 2: {self.num2}"


#Objeto donde se guarda el historial  y se realiza la operaciones
class Operaciones:

    # Constrcutor se guarda el historial en un arreglo
    def __init__(self) -> None:
        self.historial = []

    
    def suma(self, numeros):
        resultado = numeros.num1 + numeros.num2
        self.historial.append(f"Suma: {numeros.num1} + {numeros.num2} = {resultado}")
        return resultado
    

    def resta(self, numeros):
        resultado = numeros.num1 - numeros.num2
        self.historial.append(f"Resta: {numeros.num1} - {numeros.num2} = {resultado}")
        return resultado
    
    def division(self, numeros):
        if numeros.num2 == 0:
            self.historial.append(f"División: {numeros.num1} / {numeros.num2} = Error, no se puede dividir por 0")
            return "Error, no se puede dividir por 0"
        else:
            resultado = numeros.num1 / numeros.num2
            self.historial.append(f"División: {numeros.num1} / {numeros.num2} = {resultado}")
            return resultado

    def potencia(self, numeros):
        resultado = numeros.num1 ** numeros.num2
        self.historial.append(f"Potencia: {numeros.num1} ** {numeros.num2} = {resultado}")
        return resultado
    
    def raiz_cuadrada(self, numeros):
        if numeros.num1 < 0:
            self.historial.append(f"Raíz Cuadrada: Error, raíz de número negativo")
            return "Error, raíz de número negativo"
        resultado = math.sqrt(numeros.num1)
        self.historial.append(f"Raíz Cuadrada: √{numeros.num1} = {resultado}")
        return resultado

    def historial_all(self):
        for operacion in self.historial:
            print("____________________\n")
            print(operacion)
            print("____________________\n")
    
    def limpiar_historial(self):
        self.historial = []

# Ejemplo de uso
operacion = Operaciones()

numeros = Numeros(10, 0)

operacion.suma(numeros)
operacion.resta(numeros)
operacion.division(numeros)
operacion.potencia(numeros)
operacion.raiz_cuadrada(numeros)

print("___Operaciones___")
operacion.historial_all()

operacion.limpiar_historial()
print("___Historial Limpio___")
operacion.historial_all()
