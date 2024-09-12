_author_="Paula Sofia Gonzalez Zambrano"
_license_="GPL"
_version_="1.0.0"
_email_="paula.gonzalezz@campusucc.edu.co"

from Fecha import Fecha

class Empleado:
    
    # Aqui inicia la declaracion de la clase
    
    '''#----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------#'''
    
    nonmbre=""
    apellido=""
    salario=0
    
    '''#---------------------------------------------------------------
    # 1 = Masculino, 2 = Femenino
    ---------------------------------------------------------------#'''
    
    sexo=0
    
    '''#---------------------------------------------------------------
    # Asociacion
    ---------------------------------------------------------------#'''
    
    fechaIngreso = Fecha()
    fechaNacimiento = Fecha()
    
    '''#---------------------------------------------------------------
    # Metodos
    ---------------------------------------------------------------#'''
    
    # Este metodo retorna el metodo del empleado
    
    _method_ = "DarNombre"
    _parameter_ = "ninguno"
    _returns_ = "nombre"
    _Description_ = "Metodo que muestra el nombre del empleado"
    def DarNombre(self):
        # Aqui va el codigo
        return self.nombre
        
    
        _method_ = "CambiarSalario"
        _parameter_ = "nuevoSlario"
        _returns_ = "Salario"
        _Description_ = "Metodo que actualiza el salario del empleado"
    def CambiarSalario(self, nuevoSalario):
        # Aqui va el codigo
        self.salario = nuevoSalario
    
    
        # Retorna el salario del empleado
        _method_ = "DarSalario"
        _parameter_ = "ninguno"
        _returns_ = "Salario"
        _Description_ = "Metodo que muestra el salario del empleado"
    def DarSalario(self):
        # Aqui va el codigo
        return self.salario
    
    
    
    _method_ = "fechaIngreso"
    _parameter_ = "ninguno"
    _returns_ = "Dar fecha"
    _Description_ = "Metodo que regresa el metodo de otra clase"
    def ConsultarFechaIngreso(self):
        # Aqui va el codigo
        return self.fechaIngreso.DarFecha()
    
    
    _method_ = "CalcularSalarioAnual"
    _parameter_ = "ninguno"
    _returns_ = "Salario anual"
    _Description_ = "Muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        # Aqui va el codigo
        # Forma 1
        # total = self.salario*12
        # return total
        # Forma 2
        return self.salario*12
    
    _method_ = "CalcularImpuestoSalarioAnual"
    _parameter_ = "ninguno"
    _returns_ = "Impuesto del salario anual"
    _Description_ = "Muestra el impuesto del salario anual del empleado"
    def CalcularImpuestoSalarioAnual(self):
        # Aqui va el codigo
        # Forma 1
        # SalarioAnual = self.CalcularSalarioAnual()
        # impuestoAnual = SalarioAnual*0.19
        # return impuestoAnual
        # Forma 2
        return self.CalcularSalarioAnual()*0.19

    _method_ = "CalcularImpuestoSalarioMensual"
    _parameter_ = "ninguno"
    _returns_ = "Impuesto del salario mensual"
    _Description_ = "Muestra el impuesto del salario mensual del empleado"
    def CalcularImpuestoMensual(self):
        return self.DarSalario()*0.19