

class class1:
    _tim = 1
    _john = 2
    
    def tekst(self):
        print("Hallo tim heeft zoveel punten in het begin: ",self._tim)
        

werk = class1()
werk2 = class1()

werk.tekst()

werk._tim = 3

print("op werk heeft tim:",werk._tim)
print("op dag 2 heeft tim:",werk2._tim)


