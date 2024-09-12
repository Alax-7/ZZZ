_author_="Paula Sofia Gonzalez Zambrano"
_license_="GPL"
_version_="1.0.0"
_email_="paula.gonzalezz@campusucc.edu.co"

from CuentaCorriente import AhorrosTotal

class CuentAhorros:
    # Aqui inicia la declaracion de la clase
    
    '''#--------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------#'''
    
    __SaldoA = 0
    __Interes = 0.006
    
    
    '''#---------------------------------------------------------------
    # Metodos
    ---------------------------------------------------------------#'''
    
    _method_ = "ConsignarValor"
    _parameter_ = "nuevovalor"
    _returns_ = "ninguno"
    _Description_ = "Metodo que suma una consignacion al valor del saldo"
    def ConsignarValor(self, nuevoValor):
        # Aqui va el codigo
        self.__SaldoA= self.__SaldoA + nuevoValor
    
    _method_ = "DarSaldoA"
    _parameter_ = "ninguno"
    _returns_ = "saldoA"
    _Description_ = "Metodo que muestra el saldo de la cuenta"    
    def DarSaldoA(self):
        # Aqui va el codigo
        return self.__SaldoA
    
    _method_ = "RetirarValor"
    _parameter_ = "monto"
    _returns_ = "ninguno"
    _Description_ = "Metodo que permite reitar saldo de la cuenta"
    def RetirarValor(self, monto):
        # Aqui va el codigo
        self.__SaldoA = self.__SaldoA-monto
    
    
    _method_ = "DarInteresMensual"
    _parameter_ = "ninguno"
    _returns_ = "interes"
    _Description_ = "Metodo que muestra el interes de la cuenta" 
    def DarInteresMensual(self): 
        # Aqui va el codigo
        return self.__Interes*self.__SaldoA
        
        _method_ = "TotalAhorro"
        _parameter_ = "ninguno"
        _returns_ = "interes"
        _Description_ = "Metodo que calcula el total del saldo" 
    def TotalAhorro(self): 
        # Aqui va el codigo
        return self.DarInteresMensual() + self.__SaldoA
        
        
        
        
    _method_ = "ActualizarSaldoPorMes"
    _parameter_ = "ninguno"
    _returns_ = "saldo"
    _Description_ = "Metodo que actualiza el saldo"
    def ActualizarSaldoPorMes(self):
        "# Aqui va el codigo"
        
    
        
        