class tim:
    cijfer = 1
    cijfer2 = 2   
    def __init__(self, woord):
       self.woord = woord
        
    def tekst(self):
        print("hallo ik ben een", self.woord)
        
T = tim('leerling')
T.tekst()
