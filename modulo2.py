print("hola")
sumar=2+3
from abc import ABC, abstractmethod  # importar para clases abstractas



class Cliente(Entidad):
    def __init__(self, codigo, nombre, correo, telefono):
        super().__init__(codigo)  # hereda el codigo

        if not nombre:
            raise ValueError("El nombre no puede estar vacío")  # validación

        if "@" not in correo:
            raise ValueError("Correo inválido")  # validación

        if not telefono.isdigit():
            raise ValueError("El teléfono debe tener solo números")  # validación

        self.__nombre = nombre  # atributo privado
        self.__correo = correo  # atributo privado
        self.__telefono = telefono  # atributo privado

    def get_nombre(self):
        return self.__nombre  # devuelve nombre

    def get_correo(self):
        return self.__correo  # devuelve correo

    def get_telefono(self):
        return self.__telefono  # devuelve teléfono

    def mostrar_info(self):
        print(f"Código: {self._codigo} | Cliente: {self.__nombre} | Correo: {self.__correo} | Tel: {self.__telefono}")  # muestra datos


class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self._nombre = nombre  # nombre del servicio
        self._precio_base = precio_base  # precio base

    @abstractmethod
    def calcular_costo(self, *args):
        pass  # cada servicio define su cálculo

    @abstractmethod
    def mostrar_info(self):
        pass  # cada servicio muestra su info


class ServicioSala(Servicio):
    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)  # hereda datos

        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")  # validación

        self._capacidad = capacidad  # atributo propio

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")  # validación

        return self._precio_base * horas  # cálculo

    def mostrar_info(self):
        print(f"Servicio: {self._nombre} | Precio por hora: {self._precio_base} | Capacidad: {self._capacidad}")  # muestra datos


class ServicioEquipo(Servicio):
    def __init__(self, nombre, precio_base, tipo):
        super().__init__(nombre, precio_base)  # hereda datos

        if not tipo:
            raise ValueError("El tipo de equipo no puede estar vacío")  # validación

        self._tipo = tipo  # atributo propio

    def calcular_costo(self, dias):
        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")  # validación

        return self._precio_base * dias  # cálculo

    def mostrar_info(self):
        print(f"Servicio: {self._nombre} | Precio por día: {self._precio_base} | Tipo: {self._tipo}")  # muestra datos


class ServicioAsesoria(Servicio):
    def __init__(self, nombre, precio_base, tipo):
        super().__init__(nombre, precio_base)  # hereda datos

        if not tipo:
            raise ValueError("El tipo de asesoría no puede estar vacío")  # validación

        self._tipo = tipo  # atributo propio

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")  # validación

        return self._precio_base * horas  # cálculo

    def mostrar_info(self):
        print(f"Servicio: {self._nombre} | Precio por hora: {self._precio_base} | Tipo: {self._tipo}")  # muestra datos


# pruebas finales del sistema
try:
    cliente1 = Cliente(1, "Juan", "juan@email.com", "123456789")
    cliente1.mostrar_info()

    sala1 = ServicioSala("Sala de reuniones", 50, 10)
    sala1.mostrar_info()
    print("Costo sala:", sala1.calcular_costo(3))

    equipo1 = ServicioEquipo("Alquiler Laptop", 30, "Laptop")
    equipo1.mostrar_info()
    print("Costo equipo:", equipo1.calcular_costo(5))

    asesoria1 = ServicioAsesoria("Asesoría técnica", 100, "Tecnología")
    asesoria1.mostrar_info()
    print("Costo asesoría:", asesoria1.calcular_costo(2))

    # prueba con error (correo inválido)
    cliente_error = Cliente(2, "Pedro", "correo_mal", "123456")

except ValueError as e:
    print("Error:", e)  # manejo de errores

print("no teblock")