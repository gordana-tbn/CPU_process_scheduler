from process import Process
from collections import deque
import copy
class FCFS:

    def __init__(self, procesi):
        self.processes=copy.deepcopy(procesi)
        self.processes=deque(sorted(self.processes, key= lambda elem: elem.vrijeme_nailaska))

    def _launch(self):
        '''
        srednje vrijeme cekanja
        srednje vrijeme kompletiranja
        
        '''
        #vrijeme dolaska mora biti vece od 0
        vrijeme = self.processes[0].vrijeme_nailaska
        obradjeni_procesi=[]
        while self.processes:
            process=self.processes.popleft()
            process.vrijeme_cekanja= vrijeme - process.vrijeme_nailaska
            process.pocetak_izvrsavanja= vrijeme
            vrijeme+= process.vrijeme_izvrsavanja
            process.kraj_izvrsavanja= vrijeme
            process.vrijeme_kompletiranja = process.kraj_izvrsavanja - process.vrijeme_nailaska
            novi_par=(process.pocetak_izvrsavanja, process.kraj_izvrsavanja)
            process.momenti_dolaska_na_red.append(novi_par)
            obradjeni_procesi.append(process)

        return {"procesi: ": obradjeni_procesi, "srednje vrijeme kompletiranja: ": self.srednje_vrijeme_kompletiranja(obradjeni_procesi),
               "srednje vrijeme cekanja: ": self.srednje_vrijeme_cekanja(obradjeni_procesi) }
    
    def srednje_vrijeme_cekanja(self, procesi):
        ukupno_vrijeme=0
        for proces in procesi:
            ukupno_vrijeme+=proces.vrijeme_cekanja
        return ukupno_vrijeme/len(procesi)
    def srednje_vrijeme_kompletiranja(self, procesi):
        ukupno_vrijeme=0
        for proces in procesi:
            ukupno_vrijeme+=proces.vrijeme_kompletiranja
        return ukupno_vrijeme/len(procesi)
    def ispis(self):
        rjecnik_obradjenih_procesa=self._launch()
        for proces in rjecnik_obradjenih_procesa["procesi: "]:
            print(proces.to_string())
        print("Srednje vrijeme kompletiranja: "+str(rjecnik_obradjenih_procesa["srednje vrijeme kompletiranja: "]))
        print("Srednje vrijeme cekanja: "+str(rjecnik_obradjenih_procesa["srednje vrijeme cekanja: "]))
        print("-----------------------------------------------------------------------------------------------")
        self._gantova_karta(rjecnik_obradjenih_procesa)

    def _gantova_karta(self, rjecnik_obradjenih_procesa):
        for proces in rjecnik_obradjenih_procesa["procesi: "]:
            print("["+ str(proces.momenti_dolaska_na_red[0][0])+"] "+ str(proces.id), end=" ")
        print( '['+str(rjecnik_obradjenih_procesa["procesi: "][-1].momenti_dolaska_na_red[0][1])+']')