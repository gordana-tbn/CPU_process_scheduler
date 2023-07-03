from process import Process
from collections import deque
import copy

class SJF:
    def __init__(self, procesi):
        self.processes=copy.deepcopy(procesi)
        self.processes=deque(sorted(self.processes, key= lambda elem: elem.vrijeme_nailaska))
    def _launch(self):
        '''
        return:
        Obradjene procese
        Srednje vrijeme cekanja
        Srednje vrijeme kompletiranja
        '''
        vrijeme=0
        request_queue=deque([]) 
        obradjeni_procesi=[]
        while True:
            while True:
                for proces in self.processes:
                    if vrijeme >= proces.vrijeme_nailaska and proces not in obradjeni_procesi and proces not in request_queue :
                        request_queue.append(proces)
                if request_queue:
                    break 
                elif len(self.processes)!=len(obradjeni_procesi): 
                    vrijeme+=1
            request_list=list(request_queue)
            request_list.sort(key= lambda elem: elem.vrijeme_izvrsavanja)
            request_queue=deque(request_list)
            proces = request_queue.popleft()
            proces.pocetak_izvrsavanja=vrijeme
            proces.vrijeme_cekanja= vrijeme- proces.vrijeme_nailaska 
            vrijeme+=proces.vrijeme_izvrsavanja
            proces.kraj_izvrsavanja=vrijeme
            proces.vrijeme_kompletiranja=vrijeme-proces.vrijeme_nailaska
            novi_par=(proces.pocetak_izvrsavanja, proces.kraj_izvrsavanja)
            proces.momenti_dolaska_na_red.append(novi_par)
            obradjeni_procesi.append(proces)
            if len(self.processes)==len(obradjeni_procesi):    
                break 

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
        