# El empleado

class Empleado:
    pass

    def __init__(self, nombre, apellidos, dni, direccion, antiguedad, telefono, salario):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.antiguedad = antiguedad
        self.telefono = telefono
        self.salario = salario


    def imprimir(self):
        print(f"Nombre: str{self.nombre}")
        print(f"Apellidos: str{self.apellidos}")
        print(f"DNI: {self.dni}")
        print(f"Direccion: str{self.direccion}")
        print(f"Antiguedad: {self.antiguedad}")
        print(f"Telefono: {self.telefono}")
        print(f"Salario: {self.salario}")


    def incrementar(self,incremento):

        self.salario = self.salario + incremento * self.salario
        print(f"El salario sumandole el incremento es de: {self.salario}")


    imprimir()

class Secrtario(Empleado):
    pass
    def __init__(self, despacho,fax,salarioAnual,nombre,apellidos,dni,direccion,antiguedad,telefono,salario):
        super().__init__(nombre,apellidos,dni,direccion,antiguedad,telefono,salario)
        self.despacho=despacho
        self.fax=fax
        self.salarioAnual=salarioAnual


    def imprimirSecretario(self):
        print(f"Nombre: str{self.nombre}")
        print(f"Apellidos: str{self.apellidos}")
        print(f"DNI: {self.dni}")
        print(f"Direccion: str{self.direccion}")
        print(f"Antiguedad: {self.antiguedad}")
        print(f"Telefono: {self.telefono}")
        print(f"Salario: {self.salario}")
        print(f"despacho numero: {self.despacho}")
        print(f"Fax: {self.fax}")
        print(f"Salario Anual es: {self.salarioAnual}")

    imprimirSecretario()

class Vendedor:
    pass
#dar de alta al cliente
    def agregar_coche(self):
        global cliente

        id = int(input("introduzca el id:"))
        marca = str(input("introduzca que marca es:"))
        modelo = str(input("introduzca el modelo:"))

        cliente[id] = id, marca, modelo
        print(cliente)

#baja al cliente

        def delete (id):
            global cliente
            del (cliente[id])
            print("Baja cliente")

#cambiar auto

        def cambiar(id,nuevoAuto):
            print(f"el nuevo auto de {id} es {nuevoAuto}")

            