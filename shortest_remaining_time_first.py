from process import Process
from collections import deque
import copy
class SRTF:
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
        request_queue=deque() 
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
            request_list.sort(key= lambda elem: elem.preostalo_vrijeme)
            request_queue=deque(request_list)
            proces = request_queue.popleft()
            proces.preostalo_vrijeme-=1
            vrijeme+=1
            new_pair=(vrijeme-1, vrijeme)
            if proces.momenti_dolaska_na_red:
                if proces.momenti_dolaska_na_red[-1][1] - vrijeme == -1:
                    proces.momenti_dolaska_na_red[-1]=(proces.momenti_dolaska_na_red[-1][0],vrijeme)
                else:
                    proces.momenti_dolaska_na_red.append(new_pair)
            else:
                proces.momenti_dolaska_na_red.append(new_pair)

            if proces.preostalo_vrijeme==0:
                proces.vrijeme_kompletiranja=proces.momenti_dolaska_na_red[-1][1]-proces.vrijeme_nailaska   
                moment=proces.momenti_dolaska_na_red 
                if len(moment)>=2:
                    diff=0 
                    j=len(moment)-1
                    i=0           
                    while(i<j):
                        diff += moment[i + 1][0] - moment[i][1]
                        i+=1
                    proces.vrijeme_cekanja=diff+moment[0][0]-proces.vrijeme_nailaska
                else:
                    proces.vrijeme_cekanja=moment[0][0]-proces.vrijeme_nailaska
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
        obradjeni_procesi=rjecnik_obradjenih_procesa["procesi: "]
        skup_momenata=[]
        for proces in obradjeni_procesi:
            for momenti in proces.momenti_dolaska_na_red:
                skup_momenata.append(tuple(momenti)+(str(proces.id),))
        skup_momenata=sorted(skup_momenata, key=lambda elem: elem[0])
        for elem in skup_momenata:
            print("["+ str(elem[0])+"] "+ str(elem[2]), end=" ")
        print( '['+str(skup_momenata[-1][1])+']')
    