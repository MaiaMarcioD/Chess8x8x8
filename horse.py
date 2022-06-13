from turtle import pos, position
from parts import Parts


class Horse(Parts):

    def __init__( self, color ):
        super().__init__( color= color )
        self.abb= self.setAbb( "H" )

    def moveH( self, board, dimension ):
        possibilities= []

        if dimension[ 1 ]== 3:

            possibilities.append( [ ( self.pos[ 0 ]+i, self.pos[ 1 ]+j, self.pos[ 2 ] )\
                 for i,j in { 1: -2, -1: 2, 2: -1, -2: 1 }.items() \
                if len(set([ self.pos[ 0 ]+ i, self.pos[ 1 ]+ i, self.pos[ 2 ] ]).intersection(set([ i for i in range( 8 ) ])))== 3])

            possibilities.append( [ ( self.pos[ 0 ]+i, self.pos[ 1 ]+j, self.pos[ 2 ] )\
                for i,j in { 1: 2, -1: -2, 2: 1, -2: -1 }.items() \
                if len(set([ self.pos[ 0 ]+ i, self.pos[ 1 ]+ i, self.pos[ 2 ] ]).intersection(set([ i for i in range( 8 ) ])))== 3])

            possibilities.append( [ ( self.pos[ 0 ]+i, self.pos[ 1 ], self.pos[ 2 ]+ j )\
                 for i,j in { 1: -2, -1: 2, 2: -1, -2: 1 }.items() \
                if len(set([ self.pos[ 0 ]+ i, self.pos[ 1 ], self.pos[ 2 ]+ j ]).intersection(set([ i for i in range( 8 ) ])))== 3])

            possibilities.append( [ ( self.pos[ 0 ]+i, self.pos[ 1 ]+j, self.pos[ 2 ] )\
                 for i,j in { 1: 2, -1: -2, 2: 1, -2: -1 }.items() \
                if len(set([ self.pos[ 0 ]+ i, self.pos[ 1 ]+ i, self.pos[ 2 ] ]).intersection(set([ i for i in range( 8 ) ])))== 3])

        if dimension[0]== 2:
            possibilities.append( [ i for i in [] ] )
            