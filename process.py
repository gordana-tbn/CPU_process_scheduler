
class Process:

    def __init__(self, id, vrijeme_nailaska, vrijeme_izvrsavanja, prioritet):
        self.id = id
        self.vrijeme_nailaska = vrijeme_nailaska
        self.vrijeme_izvrsavanja = vrijeme_izvrsavanja
        self.prioritet = prioritet
        self.preostalo_vrijeme = vrijeme_izvrsavanja
        self.pocetak_izvrsavanja = None
        self.kraj_izvrsavanja = None
        self.momenti_dolaska_na_red=[]
        self. vrijeme_cekanja = 0
        self. vrijeme_kompletiranja = 0

    def to_string(self):
        return{"Id: {}   Vrijeme cekanja: {}     Vrijeme kompletiranja: {}".format(self.id, self.vrijeme_cekanja, self.vrijeme_kompletiranja)}
    def __str__(self):
        return {str(self.id): (self.vrijeme_nailaska, self.vrijeme_izvrsavanja, self.prioritet)}