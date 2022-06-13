
class Parts:

    def __init__(self, color, x=0, y=0, z=0 ): 
        self.color= color
        self.pos= [ x, y, z ]
        

    def setAbb( self, first ):
        """Método público: Define a abreviação do objeto;
        Entrada: Vazia
        Saída: str --> (abreviação do objeto)
        """

        if self.color==  "white":
            return f"{ first }w"

        if self.color== "black":
            return f"{ first }b"
        


    def setPos( self, x, y, z ):
        self.pos= [ x, y, z ]

    
    
    def getAbb( self ):
        """Método público: Responsável por retornar a abreviação do objeto;
        Entrada: Vazia
        Saída: str --> ( Abreviação do objeto )
    """ 
        return self.abb

    def getPos( self ):
        """Método público: Retorna o atributo pos (posição atual) do objeto
        Entranda: Vazia
        Saída: self.pos --> array unidimensional
        """
        return self.pos
    



