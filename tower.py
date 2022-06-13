from parts import Parts



class Tower(Parts):

    def __init__( self, color ):
        super().__init__( color= color )
        self.abb= self.setAbb( "T" )
        self.possibilities= []
