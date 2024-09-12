_author_="Paula Sofia Gonzalez Zambrano"
_license_="GPL"
_version_="1.0.0"
_email_="paula.gonzalezz@campusucc.edu.co"

from CuentaCorriente import CuentaCorriente
from CuentAhorros import CuentAhorros
from CDT import CDT 

class SimuladorBancario:
    
    #Aqui inicia la declaracion de la clase
    '''#----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------#'''
    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    '''#---------------------------------------------------------------
    # Asociacion
    ---------------------------------------------------------------#'''
    
    __CuentaCorrienteIngreso = CuentaCorriente()
    __CuentAhorrosIngreso = CuentAhorros()
    __CDTIngreso = CDT()
    
    '''#---------------------------------------------------------------
    # Metodos
    ---------------------------------------------------------------#'''
    
    # Permite calular el valor de todas las cuentas
    
    _method_ = "CalcularTodo"
    _parameter_ = "ninguno"
    _returns_ = "calcularTodo"
    _Description_ = "Metodo que suma el valor total del saldo de las otras cuentas"
    def CalcularTodo(self):
        # Aqui va el codigo
        return self.__CuentAhorrosIngreso.TotalAhorro()+self.__CuentaCorrienteIngreso.DarSaldoC()+self.__CDTIngreso.TotalCDT()
    
    # Nose que es esto
        _method_ = "DepositarCuentaCorriente"
        _parameter_ = "monto"
        _returns_ = "ninguno"
        _Description_ = "Metodo que permite"
    def CalcularTodo(self, monto):
        # Aqui va el codigo
        self.__CuentaCorrienteIngreso.ConsignarSaldo(monto)
        
        _method_ = "PasarAhorrosACorriente"
        _parameter_ = "ninguno"
        _returns_ = "Ninguno"
        _Description_ = "Metodo que permite pasar saldo de ahorro a la cuenta corriente"
    def PasarAhorrosACorriente(self):
        # Aqui va el codigo
        saldoAhorros = self.__CuentAhorrosIngreso.DarSaldoA()
        self.__CuentAhorrosIngreso.RetirarValor(saldoAhorros)
        self.__CuentaCorrienteIngreso.ConsignarSaldo(saldoAhorros)
        
    
        _method_ = "Ahorrar"
        _parameter_ = "monto"
        _returns_ = "Ninguno"
        _Description_ = "Metodo que permite pasar saldo de cuenta corriente a la cuenta de ahorro"
    def Ahorrar(self, monto):
        # Aqui va el codigo
        monto =  self.__CuentaCorrienteIngreso.DarSaldoC()
        self.__CuentaCorrienteIngreso.RetirarSaldo(monto)
        self.__CuentAhorrosIngreso.ConsignarValor(monto)
        
    
        _method_ = "retirarAhorro"
        _parameter_ = "monto"
        _returns_ = "ninguno"
        _Description_ = "Metodo que permite retirar un valor dado de la cuenta de ahorros"
    def RetirarAhorro(self, monto):
        # Aqui va el codigo
        self.__CuentAhorroIngreso.RetirarValor(monto)
        
    
        _method_ = "DarSaldoCorriente"
        _parameter_ = "ninguno"
        _returns_ = "DarSaldoC"
        _Description_ = "Metodo que permite retorna el saldo que hay en la cuenta corriente"
    def CalcularTodo(self):
        # Aqui va el codigo
        return self.__CuentaCorrienteIngreso.DarSaldoC()
    
        _method_ = "RetirarTodo"
        _parameter_ = "ninguno"
        _returns_ = "retirar saldo y retirar valor"
        _Description_ = "Metodo que permite retirar todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros."
    def RetirarTodo(self):
        # Aqui va el codigo
        saldoCorriente = self.__CuentaCorrienteIngreso.DarSaldoC()
        saldoAhorros = self.__CuentAhorrosIngreso.DarSaldoA()
        self.__CuentaCorrienteIngreso.RetirarSaldo(saldoCorriente)
        self.__CuentAhorrosIngreso.RetirarValor(saldoAhorros)
        
        _method_ = "DuplicarAhorro"
        _parameter_ = "ninguno"
        _returns_ = "ninguno"
        _Description_ = "Duplica la cantidad de dinero que hay en la cuenta de ahorros."
    def DuplicarAhorro(self):
        duplicar = self.__CuentAhorrosIngreso.DarSaldoA()
        self.__CuentAhorrosIngreso.ConsignarValor(duplicar)
        
    