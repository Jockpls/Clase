"""
Vehículo refactorizado - Versión Python

Problemas eliminados:
  - God Class con campos exclusivos de subclases
  - isinstance en cadena → polimorfismo con imprimir_datos_especificos()
  - Campo String tipo duplicando la jerarquía de clases → eliminado
  - calcular_impuesto() con if/else encadenado movido a cada subclase
  - Variable booleana intermedia con rama muerta → expresión directa
  - imprimir_ficha() recibía el propio objeto como parámetro → opera sobre self
  - Constructor con 10 parámetros incluyendo campos irrelevantes → eliminado
"""

from abc import ABC, abstractmethod


class Vehiculo(ABC):
    """Clase base abstracta para vehículos"""

    def __init__(self, marca: str, modelo: str, anio: int,
                 velocidad_max: float, num_ruedas: int, precio: float):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad_max = velocidad_max
        self.num_ruedas = num_ruedas
        self.precio = precio
    
    @abstractmethod
    def get_tipo_vehiculo(self) -> str:
        pass
    
    @abstractmethod
    def get_tasa_impuesto(self) -> float:
        pass
    
    @abstractmethod
    def imprimir_datos_especificos(self) -> None:
        pass
    
    def imprimir_ficha(self) -> None:
        print("=== Ficha del Vehículo ===")
        print(f"Marca   : {self.marca}")
        print(f"Modelo  : {self.modelo}")
        print(f"Año     : {self.anio}")
        print(f"Precio  : {self.precio} €")
        
        self.imprimir_datos_especificos()
        
        print(f"Antiguo : {'Sí' if self.anio < 2000 else 'No'}")
        print(f"Impuesto: {self._calcular_impuesto():.2f} €")
    
    def get_precio_con_descuento(self, descuento: float) -> float:
        return self.precio - (self.precio * descuento)
    
    def _calcular_impuesto(self) -> float:
        return self.precio * self.get_tasa_impuesto()


class Coche(Vehiculo):
    """Clase para coches"""
    
    def __init__(self, marca: str, modelo: str, anio: int,
                 velocidad_max: float, precio: float, num_puertas: int):
        super().__init__(marca, modelo, anio, velocidad_max, 4, precio)
        self.num_puertas = num_puertas
    
    def get_tipo_vehiculo(self) -> str:
        return "COCHE"
    
    def get_tasa_impuesto(self) -> float:
        return 0.21
    
    def imprimir_datos_especificos(self) -> None:
        print(f"Puertas : {self.num_puertas}")
        print(f"Vel.Max : {self.velocidad_max} km/h")


class Moto(Vehiculo):
    """Clase para motos"""
    
    def __init__(self, marca: str, modelo: str, anio: int,
                 velocidad_max: float, precio: float, tiene_sidecar: bool):
        super().__init__(marca, modelo, anio, velocidad_max, 2, precio)
        self.tiene_sidecar = tiene_sidecar
    
    def get_tipo_vehiculo(self) -> str:
        return "MOTO"
    
    def get_tasa_impuesto(self) -> float:
        return 0.15
    
    def imprimir_datos_especificos(self) -> None:
        print(f"Sidecar : {'Sí' if self.tiene_sidecar else 'No'}")
        print(f"Vel.Max : {self.velocidad_max} km/h")


class Camion(Vehiculo):
    """Clase para camiones"""
    
    def __init__(self, marca: str, modelo: str, anio: int,
                 velocidad_max: float, precio: float, capacidad_carga: float):
        super().__init__(marca, modelo, anio, velocidad_max, 18, precio)
        self.capacidad_carga = capacidad_carga
    
    def get_tipo_vehiculo(self) -> str:
        return "CAMION"
    
    def get_tasa_impuesto(self) -> float:
        return 0.10
    
    def imprimir_datos_especificos(self) -> None:
        print(f"Carga   : {self.capacidad_carga} t")
        print(f"Ruedas  : {self.num_ruedas}")
