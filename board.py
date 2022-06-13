
from parts import Parts
from king import King
from pawn import Pawn



class Board:

    def __init__( self ):
        self.array= []
        self.space= []
        self.di= {}
        self.setB()

    def f( self, k, j, i ):
        """Método privado (alterar posteriormente): Responsável por definir as cores do tabuleiro
        Entrada: k, j, i --> ( Posições no eixo Z/ Y/ X respectivamente )
        Saída: 1/ 0 --> ( 1= Branco /2= Preto )"""

        if (( k+ j+ i )% 2== 0 ):
            return 0

        if (( k+ j+ i )% 2!= 0 ):
            return 1
        
    def setB( self ):
            """Método privado (alterar posteriormente): Responsável pela criação do tabuleiro.
            Entrada: Vazia
            Saída: Vazia"""

            list2= []
            list3= []

            for k in range( 1, 9 ):
                for j in range( 1, 9 ):
                    for i in range( 1, 9 ):
                        list2.append( self.f( k, j, i ) )

                    list3.append( list2 )
                    list2= []
                self.array.append( list3 )
                list3= []

    def showB( self ):
        """Métedo privado (alterar posteriormente): Responsável por mostrar o tabuleiro;
        Entrada: Vazia
        Saída: Vazia """

        u= ""
        for z in self.array:
            for y in z:
                for x in y:
                    if x in [ 1, 0 ]:
                        u+= f" { x } "
                    if x not in [ 1, 0 ]:
                        u+= f"{ x.getAbb() } "
                u+= "\n"
            u+= "\n"
        print( u )

    def getBo( self, typee ):
        """Método público: Responsável por devolver a matriz atualizada do tabuleiro ao ser chamada;
        Entrada: typee --> ( 1= Dicionário ou 2= lista )
        Saída: dict/list --> ( dict/ list )
        """

        if typee== 1:
            return self.di

        if typee== 2:
            return self.array

    def getProg( self ):
        """Método público: Responsável por retornar as projeções de cada peça;
        Entrada: Vazia
        Saída: list
        """

        return self.space

    def setPos( self, z, y, x, part, pos ):
        """Métdodo público: Responsável por alterar as peças do tabuleiro;
        Entradas: z, y, x, part -->  ( posições no eixo z[ 0: 7 ]/ y[ 0: 7 ]/ x[ 0: 7 ]
         desejadas ( respectivamente ), part= objeto a ser alocado )
        Saída: Vazia
        """
        
        if self.array[z][y][x] in [1,0] and pos == True:
            self.array[z][y][x]= part

    
    def whichIs( self, coor, obj ):
        
        spam= [ i for i in range( 8 ) ]
        if (coor[0] in spam) and (coor[ 1 ] in spam) and (coor[ 2 ] in spam):

            item= self.array[ coor[ 0 ] ][ coor[ 1 ] ][ coor[ 2 ] ]            

            if ( type( obj ) == King ) and ( ( type( item ) == Parts and item.getAbb() != obj.getAbb() ) or ( item in [ 1, 0 ] ) ):

                return True

            if ( type( obj ) == Pawn ) and( ( type( item ) == int and coor[ 2 ] == obj.getPos()[ 2 ] ) or ( type( item ) != int and item.color != obj.color )):
                return True

        else:
            return False