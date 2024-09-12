_author_="Paula Sofia Gonzalez Zambrano"
_license_="GPL"
_version_="1.0.0"
_email_="paula.gonzalezz@campusucc.edu.co"

from CuentaCorriente import CuentaCorriente

class CDT:
    
    #Aqui inicia la declaracion de la clase
    '''#-------------------------------------------------------------
    # Atributos
    -------------------------------------------------------------#'''
    
    __InteresT = 0
    __SaldoT = 0
    EstadoT = 0
    
    '''#---------------------------------------------------------------
    # Asociacion
    ---------------------------------------------------------------#'''
    
    CuentaCorrienteIngreso = CuentaCorriente()

    '''#---------------------------------------------------------------
    # Metodos
    ---------------------------------------------------------------#'''

    _method_ = "DarSaldoT"
    _parameter_ = "ninguno"
    _returns_ = "saldoT"
    _Description_ = "Metodo que muestra el saldo de la cuenta"    
    def DarSaldoT(self):
        # Aqui va el codigo
        return self.__SaldoT
    
        _method_ = "DarInteresMensual"
        _parameter_ = "ninguno"
        _returns_ = "interes"
        _Description_ = "Metodo que muestra el interes de la cuenta" 
    def DarInteresMensual(self): 
        # Aqui va el codigo
        return self.__InteresT*self.__SaldoT
        
        _method_ = "TotalCDT"
        _parameter_ = "ninguno"
        _returns_ = "interes"
        _Description_ = "Metodo que calcula el total del saldo" 
    def TotalCDT(self): 
        # Aqui va el codigo
        return self.DarInteresMensual()+self.__SaldoA