_author_="Paula Sofia Gonzalez Zambrano"
_license_="GPL"
_version_="1.0.0"
_email_="paula.gonzalezz@campusucc.edu.co"
from CuentAhorros import CuentAhorro
class CuentaCorriente:
    # Aqui inicia la declaracion de la clase
    '''#----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------#'''
    
    __SaldoC = 0 
     
    

    '''#---------------------------------------------------------------
    # Metodos
    ---------------------------------------------------------------#'''
    _method_ = "DarSaldoC"
    _parameter_ = "ninguno"
    _returns_ = "saldoC"
    _Description_ = "Metodo que muestra el saldo de la cuenta"    
    def DarSaldoC(self):
        # Aqui va el codigo
        return self.SaldoC

    _method_ = "RetirarSaldo"
    _parameter_ = "monto"
    _returns_ = "ninguno"
    _Description_ = "Metodo que permite retirar saldo de la cuenta"
    def RetirarSaldo(self, monto):
        # Aqui va el codigo
        self.__SaldoC= self.__SaldoC-monto
    
    _method_ = "ConsignarSaldo"
    _parameter_ = "monto"
    _returns_ = "ninguno"
    _Description_ = "Metodo que Permite consignar un monto a la cuenta corriente"
    def ConsignarSaldo(self, monto):
        # Aqui va el codigo
        self.__SaldoC= self.__SaldoC + monto
        
    
        
