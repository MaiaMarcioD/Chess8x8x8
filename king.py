from parts import Parts



class King( Parts ):


    def __init__( self, color ):
        super().__init__( color= color )
        self.abb= self.setAbb( "K" )
        self.possibilities= []


    def moveK( self, board ):
        """Método público: Define as possíveis casas do rei (Incompleto (Acrescentar impossíbilidades de projeções de outras peças))
            Entrada: board --> board (Tabuleiro da partida)
            Saída: Vazia
        """
        
        p= ( self.pos[ 0 ], self.pos[ 1 ], self.pos[ 2 ] )
        spam= [i for i in range( 8 ) ]
        self.possibilities.append( [ [ p[ 0 ], p[ 1 ]+ int( v[ 0 ] ), p[ 2 ]+ v[ 1 ]] for u,v  in \
            { -1: [ -1, 1 ], 1: [1, -1], 1.1: [ 1, 1 ] , -1.1: [ -1, -1 ], 1.2 :[ 1, 0 ], -1.2: [ -1, 0 ], 0: [ 0, 1 ], 0.1: [ 0, -1 ] }.items()\
            if p[ 1 ] + int( v[ 0 ] ) in spam and p[ 2 ] + v[ 1 ] in spam and ( board.whichIs([p[ 0 ], p[ 1 ]+ v[ 0 ], p[ 2 ]+ v [ 1 ] ], self ) == True)])




        