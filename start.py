from keyword import kwlist
from parts import Parts
from pawn import Pawn
from horse import Horse
from bishop import Bishop
from queen import Queen
from king import King
from tower import Tower
from board import Board

def setPW( board, list ):
    [ board.setPos( 0, 1, list.index( i ), list[list.index( i )], True ) for i in list ]
    [ i.setPos( 0, 1, list.index( i )) for i in list ]
    

def setPB( board, list ):
    [ board.setPos( 0, 6, list.index( i ), list[list.index( i )], True ) for i in list ]
    [ i.setPos( 0, 6, list.index( i )) for i in list ]

def start( board ):


    # Peças brancas

    Twhite= [ Tower( 'white' ) for i in range( 2 ) ]
    Pwhite= [ Pawn( "white" ) for i in range( 8 ) ]
    Hwhite= [ Horse( "white") for i in range( 2 )  ]
    Bwhite= [ Bishop( "white" ) for i in range( 2 ) ]
    Qwhite= Queen( "white" )
    Kwhite= King( "white" )


        # Posicionamentos peças brancas
            # Torres brancas
    board.setPos( 0, 0, 0, Twhite[ 0 ], True )
    board.setPos( 0, 0, 7, Twhite[ 1 ], True )
    Twhite[0].setPos( 0, 0, 0 )
    Twhite[1].setPos( 0, 0, 7 )


            # Pawn brancos
    setPW( board, Pwhite )


            # Cavalos brancos
    board.setPos( 0, 0, 1, Hwhite[ 0 ], True )
    board.setPos( 0, 0, 6, Hwhite[ 1 ], True )
    Hwhite[0].setPos( 0, 0, 1 )
    Hwhite[1].setPos( 0, 0, 6 )


            # Bispos brancos
    board.setPos( 0, 0, 5, Bwhite[ 0 ], True )
    board.setPos( 0, 0, 2, Bwhite[ 1 ], True )
    Bwhite[0].setPos( 0, 0, 5 )
    Bwhite[1].setPos( 0, 0, 2 )

            # Dama e Rei brancos
    board.setPos( 0, 0, 3, Kwhite, True )
    board.setPos( 0, 0, 4, Qwhite, True )
    Kwhite.setPos( 0, 0, 3 )
    Qwhite.setPos( 0, 0, 4 )
    

    # Peças negras
    Tblack= [ Tower( 'black' ) for i in range( 2 ) ]
    Pblack= [ Pawn( "black" ) for i in range( 8 ) ]
    Hblack= [ Horse( "black") for i in range( 2 ) ]
    Bblack= [ Bishop( "black" ) for i in range( 2 ) ]
    Qblack= Queen( "black" )
    Kblack= King( "black" )


        # Posicionamento peças negras
            # Torres negras
    board.setPos( 0, 7, 0, Tblack[ 0 ], True )
    board.setPos( 0, 7, 7, Tblack[ 1 ], True )
    Tblack[ 0 ].setPos( 0, 7, 0 )
    Tblack[ 1 ].setPos( 0, 7, 7 )


            # Pawn negros
    setPB( board, Pblack )


            # Cavalos negros
    board.setPos( 0, 7, 1, Hblack[ 0 ], True )
    board.setPos( 0, 7, 6, Hblack[ 1 ], True )
    Hblack[ 0 ].setPos( 0, 7, 1 )
    Hblack[ 1 ].setPos( 0, 7, 6 )


            # Bispos negros
    board.setPos( 0, 7, 5, Bblack[ 0 ], True )
    board.setPos( 0, 7, 2, Bblack[ 1 ], True )
    Bblack[ 0 ].setPos( 0, 7, 5 )
    Bblack[ 1 ].setPos( 0, 7, 2 )


            # Dama e Rei negros
    board.setPos( 0, 7, 3, Kblack, True )
    board.setPos( 0, 7, 4, Qblack, True )
    Kblack.setPos( 0, 7, 3 )
    Qblack.setPos( 0, 7, 4 )

    board.setPos( 0, 2, 1, Pblack[0], True )
    Pblack[ 0 ].setPos( 0, 2, 1 )
    Pwhite[ 0 ].moveP(board)
    print( Pwhite[ 0 ].possibilities )
    
    Pblack[ 0 ].moveP(board)
    print( Pblack[ 0 ].possibilities )
    board.showB()