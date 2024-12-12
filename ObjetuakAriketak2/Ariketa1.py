class Dokumentua:
    def __init__(self):
        self.testua = ""

    def Idatzi(self, testua):
        self.testua += testua

    def __str__(self):
        return self.testua


class Papel(Dokumentua):
    def __init__(self):
        super().__init__()

    def Idatzi(self, testua):
       
        super().Idatzi(testua)


papel = Papel()
papel.Idatzi("Papereko testua. ")
papel.Idatzi("Testu gehiago.")
print(papel)
