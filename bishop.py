from parts import Parts



class Bishop(Parts):

    def __init__( self, color ):
        super().__init__( color= color )
        self.abb= self.setAbb( "B" )


