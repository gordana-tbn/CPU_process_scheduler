from fcfs import FCFS
from prioritet import Priorty
from shortest_job_first import SJF
from shortest_remaining_time_first import SRTF
from rr import Round_Robin
from process import Process
import copy
import json

def execute_from_file(file_path):
    data_dict={}
    with open(file_path, 'r') as fp:
        data_dict = json.load(fp)
    br_procesa=data_dict["broj procesa"]
    process_dict=data_dict["procesi:"]
    algoritmi=data_dict["algoritam"]
    algoritmi=algoritmi.split(',')
    procesi=[]
    for key,value in process_dict.items():
        procesi.append(Process((key), value[0], value[1], value[2]))
    for algoritam in algoritmi:
        if algoritam=="shortest job first":
            algoritam_za_izvrsavanje=SJF(procesi)
        elif algoritam=="round robin":
            algoritam_za_izvrsavanje=Round_Robin(procesi)
        elif algoritam=="prioritet":
            algoritam_za_izvrsavanje=Priorty(procesi)
        elif algoritam=="shortest remaining time first":
            algoritam_za_izvrsavanje=SRTF(procesi)
        elif algoritam=="first come first serve":
            algoritam_za_izvrsavanje=FCFS(procesi) 
        else:
            raise ValueError("Neispravan unos naziva algoritma!")
        algoritam_za_izvrsavanje.ispis()

mode=input('''Unesite nacin izvrsavanja:
                    [0] Ucitavanje iz fajla.
                    [1] Rucni unos podataka
            ''')
if mode=='0':
    file_path=input("Unesite ispravnu putanju fajla:")
    execute_from_file(file_path)
elif mode=='1':
    print("""Ispravni nazivi algoritama za rad sa fajlom
    "shortest job first"
    "round robin"
    "prioritet"
    "shortest remaining time first"
    "first come first serve" """)
    broj_procesa=int(input("Unesite broj procesa:"))
    procesi=[]
    while(broj_procesa>0):
        id=input("Unesite id procesa:")
        vrijeme_nailaska=int(input("Unesite vrijeme nailaska procesa:"))
        vrijeme_izvrsavanja=int(input("Unesite vrijme izvrsavanja procesa:"))
        prioritet=int(input("Unesite prioritet procesa:"))
        procesi.append(Process(id, vrijeme_nailaska, vrijeme_izvrsavanja, prioritet))
        broj_procesa-=1
    print("""Ispravni nazivi algoritama za rad sa fajlom:
    "shortest job first,round robin,prioritet,shortest remaining time first,first come first serve" """)
    algoritmi=input("Unesite zeljene algoritme(unijeti malim slovima, razdvojene ','):")
    algoritmi=algoritmi.split(',')
    for algoritam in algoritmi:
            if algoritam=="shortest job first":
                algoritam_za_izvrsavanje=SJF(procesi)
            elif algoritam=="round robin":
                algoritam_za_izvrsavanje=Round_Robin(procesi)
            elif algoritam=="prioritet":
                algoritam_za_izvrsavanje=Priorty(procesi)
            elif algoritam=="shortest remaining time first":
                algoritam_za_izvrsavanje=SRTF(procesi)
            elif algoritam=="first come first serve":
                algoritam_za_izvrsavanje=FCFS(procesi) 
            else:
                raise ValueError("Neispravan unos naziva algoritma!")
            algoritam_za_izvrsavanje.ispis()
else:
    print("Kraj rada")
#execute_from_file(r"C:\Users\tubon\Desktop\oos_projekat\out.txt")

'''
p1= Process("p1", 0, 7, 1)
p2= Process("p2", 2, 4, 2) 
p3= Process("p3", 4, 1, 3)
p4= Process("p4", 5, 4, 4) 

procesi=[p1, p2, p3, p4]

fcfs=FCFS(procesi)
prioritet=Priorty(procesi)
sjf=SJF(procesi)
srtf=SRTF(procesi)
rr=Round_Robin(procesi)

sjf.ispis()
srtf.ispis()
'''
