"""
Employee refactorizado - Versión Python

Técnicas aplicadas:
  1. Extraer clase → Address, SalaryInfo, ContactInfo, BonusCalculator
  2. Extraer metodo → print_employee_report() delega a 3 métodos privados
  3. Pasar objeto completo → get_monthly_salary(SalaryInfo) en lugar de 2 primitivos
  4. Simplificar condicional: return age > 30
"""

from dataclasses import dataclass


@dataclass
class Address:
    """Clase para datos de dirección"""
    country: str
    city: str
    street: str
    house: str
    quarter: str
    
    def get_full_address(self) -> str:
        return f"{self.country}, {self.city}, {self.street}, {self.house} {self.quarter}"


@dataclass
class SalaryInfo:
    """Clase para datos de salario"""
    yearly_salary: float
    awards: float
    currency: str
    payment_date: str
    
    def get_monthly_salary(self) -> float:
        return (self.yearly_salary + self.awards) / 12
    
    def get_formatted_monthly_salary(self) -> str:
        monthly = self.get_monthly_salary()
        return f"{monthly:.2f} {self.currency}"
    
    def get_currency(self) -> str:
        return self.currency
    
    def get_payment_date(self) -> str:
        return self.payment_date


@dataclass
class ContactInfo:
    """Clase para datos de contacto"""
    phone_country_code: str
    phone_area_code: str
    phone_number: str
    
    def get_formatted_phone(self) -> str:
        return f"+{self.phone_country_code} ({self.phone_area_code}) {self.phone_number}"


class BonusCalculator:
    """Calculadora de bonos según edad"""
    
    def calculate(self, monthly_salary: float, age: int) -> float:
        if age < 25:
            return monthly_salary * 0.05
        elif age < 40:
            return monthly_salary * 0.10
        elif age < 55:
            return monthly_salary * 0.15
        else:
            return monthly_salary * 0.20


class Employee:
    """Clase principal de empleado"""
    
    def __init__(self, name: str, age: int,
                 address: Address,
                 salary_info: SalaryInfo,
                 contact_info: ContactInfo):
        self._name = name
        self._age = age
        self._address = address
        self._salary_info = salary_info
        self._contact_info = contact_info
        self._bonus_calculator = BonusCalculator()
    
    def print_employee_report(self) -> None:
        """Método principal que coordina la impresión del reporte"""
        print("=== Reporte de Empleado ===")
        self._print_personal_info()
        self._print_contact_details()
        self._print_salary_details()
    
    def _print_personal_info(self) -> None:
        print(f"Nombre   : {self._name}")
        print(f"Edad     : {self._age}")
        print(f"Dirección: {self._address.get_full_address()}")
    
    def _print_contact_details(self) -> None:
        print(f"Teléfono : {self._contact_info.get_formatted_phone()}")
    
    def _print_salary_details(self) -> None:
        monthly = self._salary_info.get_monthly_salary()
        bonus = self._bonus_calculator.calculate(monthly, self._age)
        print(f"Salario mensual: {self._salary_info.get_formatted_monthly_salary()}")
        print(f"Bono           : {bonus:.2f} {self._salary_info.get_currency()}")
        print(f"Fecha de pago  : {self._salary_info.get_payment_date()}")
    
    def get_monthly_salary(self, salary_info: SalaryInfo) -> float:
        return salary_info.get_monthly_salary()
    
    def is_eligible_for_promotion(self) -> bool:
        return self._age > 30
    
    # Propiedades (getters)
    @property
    def name(self): return self._name
    
    @property
    def age(self): return self._age
    
    @property
    def address(self): return self._address
    
    @property
    def salary_info(self): return self._salary_info
    
    @property
    def contact_info(self): return self._contact_info
