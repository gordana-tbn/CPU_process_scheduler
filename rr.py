from process import Process
from collections import deque
import copy
class Round_Robin:

    def __init__(self, procesi, kvant=1):
        self.processes=copy.deepcopy(procesi)
        self.processes=deque(sorted(self.processes, key= lambda elem: elem.vrijeme_nailaska))
        self.kvant = kvant
    
    def _launch(self):
        '''
        srednje vrijeme cekanja
        srednje vrijeme kompletiranja
        '''
        vrijeme = 0
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
            proces = request_queue.popleft() 
            self.processes.remove(proces)
            self.processes.append(proces)
            if proces.preostalo_vrijeme > self.kvant :
                proces.preostalo_vrijeme-=self.kvant
                for elem in request_queue:
                    if elem!= proces:
                        elem.vrijeme_cekanja+=self.kvant
                moment=vrijeme
                vrijeme+=self.kvant
            else:   
                moment=vrijeme
                vrijeme+=proces.preostalo_vrijeme
                for elem in request_queue:
                    if elem!= proces:  #nece ga biti u redu jer je skinut na pocetku
                        elem.vrijeme_cekanja+=proces.preostalo_vrijeme
                proces.preostalo_vrijeme=0
                proces.vrijeme_kompletiranja= vrijeme - proces.vrijeme_nailaska
                obradjeni_procesi.append(proces)
            new_pair=(moment, vrijeme)
            proces.momenti_dolaska_na_red.append(new_pair)

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
        obradjeni_procesi=rjecnik_obradjenih_procesa["procesi: "]
        skup_momenata=[]
        for proces in obradjeni_procesi:
            for momenti in proces.momenti_dolaska_na_red:
                skup_momenata.append(tuple(momenti)+(str(proces.id),))
        skup_momenata=sorted(skup_momenata, key=lambda elem: elem[0])
        for elem in skup_momenata:
            print("["+ str(elem[0])+"] "+ str(elem[2]), end=" ")
        print( '['+str(skup_momenata[-1][1])+']')
        
