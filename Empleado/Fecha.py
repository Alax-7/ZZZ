_author_="Paula Sofia Gonzalez Zambrano"
_license_="GPL"
_version_="1.0.0"
_email_="paula.gonzalezz@campusucc.edu.co"
class fecha:
    
    # Aqui inicia la declaracion de la clase
    
    '''#---------------------------------------------------------------
    # Atributos
    ---------------------------------------------------------------#'''
    
    dia=0
    mes=0
    anio=0
    
    '''#---------------------------------------------------------------
    # Metodos
    ---------------------------------------------------------------#'''
    
    
    _method_ = "DarDia"
    _parameter_ = "ninguno"
    _returns_ = "dia"
    _Description_ = "Metodo que regresa el dia"
    def DarDia(self):
        # Aqui va el codigo
        return self.dia
        
        
        
        
        _method_ = "DarMes"
        _parameter_ = "ninguno"
        _returns_ = "mes"
        _Description_ = "Metodo que regresa el mes"
    def DarMes(self):
        # Aqui va el codigo
        return self.mes
        
        
        
        
        _method_ = "DarAnio"
        _parameter_ = "ninguno"
        _returns_ = "anio"
        _Description_ = "Metodo que regresa el año"
    def DarAnio(self):
        # Aqui va el codigo
        return self.anio
    
    _method_ = "DarFecha"
    _parameter_ = "ninguno"
    _returns_ = "La fecha de la clase"
    _Description_ = "Metodo que regresa la fecha digitada por el usuario"
    def DarFecha(self):
        # Aqui va el codigo
        return self.dia+'/'+self.mes+'/'+self.anio
    
    
        