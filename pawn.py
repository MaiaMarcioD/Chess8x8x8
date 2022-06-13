from parts import Parts



class Pawn(Parts):

    def __init__( self, color ):
        super().__init__( color= color )
        self.abb= self.setAbb( "P" )
        self.first= True
        self.possibilities= []



    def moveP( self, board):
        p= [ self.pos[ 0 ], self.pos[ 1 ], self.pos[ 2 ] ]
        if self.first == True:
            self.possibilities.append( [ [ p[ 0 ], p[ 1 ]+ j, p[ 2 ]+ int( i ) ] for i,j in \
                { 1: 0, 2: 0, 1.11: -1, 1.1: 1, -1: 0, -2: 0, -1.1: -1, -1.11: 1 }.items() \
                if ( [ board.whichIs( [ p[ 0 ], p[ 1 ]+ int( i ), p[ 2 ]+ j ], self ) ][ 0 ] == True ) ] )
