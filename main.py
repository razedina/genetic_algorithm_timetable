import random as random
from tabulate import tabulate
import copy
import operator
import time
import numpy as np
import matplotlib.pyplot as plt

profe = {
        1 : "Narcis Behlilovic",
        2 : "Huse Fatkic",
        3 : "Vedran Ljubovic",
        4 : "Almasa Odzak",
        5 : "Hasnija Samic",
        6 : "Senad Huseinbegovic",
        7 : "Zeljko Juric",
        8 : "Dinko Osmankovic",
        9 : "Samir Ribic",
        10 : "Abdulah Aksamovic",
        11 : "Tarik Uzunovic",
        12 : "Alija Muharemovic",
        14 : "Alma Omerspahic",
        15 : "Smajo Bisanovic",
        16 : "Mujo Hebibovic",
        17 : "Bakir Lacevic",
        18 : "Jasmin Velagic",
        19 : "Nasuf Hadziahmetovic",
        20 : "Dzenana Djonko",
        21 : "Samim Konjicija",
        22 : "Emir Sokic",
        23 : "Mustafa Music",
        24 : "Sead Kreso",
        25 : "Semsudin Masic",
        26 : "Adnan Tahirovic",
        27 : "Dusanka Boskovic",
        28 : "Haris Supic",
        29 : "Razija Turcinhodzic",
        30 : "Novica Nosovic",
        31 : "Emir Buza",
        32 : "Vensada Okanovic",
        33 : "Kemal Hajdarevic",
        34 : "Amila Akagic",
        35 : "Anel Tanovic",
        36 : "Zikrija Avdagic",
        37 : "Sasa Mrdovic",
        38 : "Ingmar Besic",
        39 : "Selma Hanjalic",
        40 : "Mirza Batalovic",
        41 : "Hamid Zildzo",
        42 : "Adnan Mujezinovic",
        43 : "Mirsad Kapetanovic",
        44 : "Tatjana Konjic",
        45 : "Senad Smaka",
        46 : "Zijad Bajramovic",
        47 : "Selma Grebovic",
        48 : "Samir Omanovic",
        49 : "Selma Rizvic"
}


grupe = {
        1 : "AiE1",
        2 : "AiE2",
        3 : "AiE3",
        4 : "AiE4",
        12 : "RI2",
        13 : "RI3",
        14 : "RI4",
        22 : "EE2",
        23 : "EE3"
}




#AiE subjects, 7 + 8 + 8 + 5 + 6 +6 = 40 predmeta

#[10, 2, "AE"], [11, 2, "SIM"], [12, 2, "EMJ"], [14, 2, "IM3"], [15, 2, "EK2"], [7, 2, "DM"], [8, 2, "DS2"]
#[16, 2, "LSAU"], [6, 2, "DE"], [17, 2, "MIS"], [18, 2, "AKT"], [19, 2, "OPTO"], [20, 2, "OOAD"], [21, 2, "PAI"], [10, 2, "PEE"]

#[22, 3, "SIS"], [22, 3, "PLS"], [16, 3, "DSU"], [23, 3, "DIK"], [21, 3, "PA"], [10, 3, "PE"], [6, 3, "OEE"], [20, 3, "RPR"]
#[24, 3, "SRES"], [22, 3, "PMS"], [17, 3, "ROB"], [18, 3, "MEH"], [25, 3, "DFTS"]

#[16, 4, "NSAU"], [26, 4, "DOS"], [27, 4, "DRAOS"], [21, 4, "OR"], [28, 4, "MMS"], [18, 4, "DS4"]
#[27, 4, "BSS"], [10, 4, "NEKS"], [21, 4, "OU"], [8, 4, "PIP"], [17, 4, "IS"], [29, 4, "OI"]

#RI subjects dodano 5 + 9 + 4 + 3 + 5 + 3 = 29
#[7, 12, "NA"], [7, 12, "DMri"], [30, 12, "LD"], [31, 12, "OBP"], [28, 12, "ASP"]
#[30, 12, "RA"], [20, 12, "OOAD"], [28, 12, "AFJ"], [32, 12, "RMA"], [21, 12, "US"], [33, 12, "ORM"], [34, 12, "DSP"], [38, 12, "CCI"], [39, 12, "IEK"]

#[29, 13, "OOI"], [35, 13, "OIS"], [32, 13, "WT"], [9, 13, "PJP"]
#[30, 13, "SI"], [36, 13, "VI"], [37, 13, "ARM"]

#[31, 14, "BP"], [30, 14, "PRS"], [48, 14, "POOS"], [29, 14, "OI"], [37, 14 "RM"]
#[35, 14, "PPIS"], [49, 14, "NGA"], [48, 14, "NSSI"]

#EE 4 + 5 + 6 + 6 =  21
#[40, 22, "PEES"], [41, 22, "IE"], [15, 22, "OES"], [42, 22, "EMJ2"]
#[5, 22, "EMAT"], [39, 22, "IEEK"], [16, 22, "OSAU"], [43, 22, "OMEH"], [11, 22, "SIP"]

#[40, 23, "TVNI"], [44, 23, "ES"], [41, 23, "PEE1"], [45, 23, "ELMS"], [46, 23, "TVI"], [47, 23, "EISM"] 
#[47, 23, "ESIT"], [47, 23, "ESP"], [47, 23, "EPOS"], [25, 23, "EPOG"], [45, 23, "PREE"], [44, 23, "UPEE"]






#self.predmeti = list ([10, 2, "AE"], [11, 2, "SIM"], [12, 2, "EMJ"], [14, 2, "IM3"], [15, 2, "EK2"], [7, 2, "DM"], [8, 2, "DS2"],  [16, 2, "LSAU"], [6, 2, "DE"], [17, 2, "MIS"], [18, 2, "AKT"], [19, 2, "OPTO"], [20, 2, "OOAD"], [21, 2, "PAI"], [10, 2, "PEE"], [22, 3, "SIS"], [22, 3, "PLS"], [16, 3, "DSU"], [23, 3, "DIK"], [21, 3, "PA"], [10, 3, "PE"], [6, 3, "OEE"], [20, 3, "RPR"], [24, 3, "SRES"], [22, 3, "PMS"], [17, 3, "ROB"], [18, 3, "MEH"], [25, 3, "DFTS"], [16, 4, "NSAU"], [26, 4, "DOS"], [27, 4, "DRAOS"], [21, 4, "OR"], [28, 4, "MMS"], [18, 4, "DS4"],  [27, 4, "BSS"], [10, 4, "NEKS"], [21, 4, "OU"], [8, 4, "PIP"], [17, 4, "IS"], [29, 4, "OI"], [7, 12, "NA"], [7, 12, "DMri"], [30, 12, "LD"], [31, 12, "OBP"], [28, 12, "ASP"]  )



# -100 ako ima poklapanja
# -1 ako profa ima 2 za redom
# -5 ako profa ima 3 za redom
# -1 ako studenti imaju 3 za redom
# -2.5 ako studenti imaju pauzu izmedju SAMO

def generisanje_srednjih_clanova(x, b=1):
    a=[[],[],[],[],[]]
    for red in x:
        for i in range(1,len(red),3):
            a[int(i/3)].append(red[i][b])
    return list(a)

class Raspored:
    def __init__(self):
        self.hromozom=[]
        self.fitness = 0
        self.problem1 = [0, 0]#uvodim ove dvije kako bih u mutaciji znala sta smeta
        self.problem2=[0, 0]#zbog ukrstanja
        self.preklapanja=[0,0,0,0,0]#
    
    def Get_fitness(self):
        return self.fitness

    def Evaluiraj_fitness(self):
        br_sala=len(self.hromozom)
        po_danima=len(self.hromozom[0])#prema ideji bi vazda trebalo biti 15
        vrijednost = 0
        kazna = [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]
        provjera = list(generisanje_srednjih_clanova(self.hromozom))
        provjera_profe = list(generisanje_srednjih_clanova(self.hromozom,0))

        for i in range(len(self.hromozom)): #br_sala
            red1 = self.hromozom[i]   #red1 je [[1, 2, 'PAI'], [4, 3, 'SREES'], [1, 3, 'PA/PE'], [2, 2, 'LSAU']]
            #  poredimo prvi red sa ostalima
            for j in range(i,br_sala): #ostavim i da se znatno vrijeme izvrsanja reducira
                red2=self.hromozom[j]
                for k in range(po_danima):
                    if (i != j):
                        if red1[k][0] == red2[k][0]: # razdvojiti na 3 ifa da ukoliko je vece preklapanje dadne manji fitess
                            vrijednost = vrijednost - 100
                            #print(profe[red1[k][0]], grupe[red1[k][1]], "profe",red1[k][2],i,k )
                            self.problem1=[i, k]
                            self.preklapanja[int(k/3)]=self.preklapanja[int(k/3)]+1
                            #print("problem", self.hromozom[i][k])              
                        if red1[k][1] == red2[k][1]:
                            vrijednost = vrijednost - 100
                            self.problem2=[i,k] #mala je sansa da problem1 bude isti kao problem2
                            #print(profe[red1[k][0]], grupe[red1[k][1]], "studenti",red1[k][2], i,k )
                            self.preklapanja[int(k/3)]=self.preklapanja[int(k/3)]+1
                            #print("problem", self.hromozom[i][k])   
                        if red1[k][2] == red2[k][2]:
                            vrijednost = vrijednost- 100
                            self.preklapanja[int(k/3)]=self.preklapanja[int(k/3)]+1
                            #print(profe[red1[k][0]], grupe[red1[k][1]], "predmeti" )

                    if k % 3 == 0:
                        # 0 oznacava profe
                            

                        if red1[k][0] == red2[k+2][0] and red1[k][0] in provjera_profe[int(k/3)]:
                             #profe imaju 3 casa zaredom
                            kazna[int(k/3)][0] = kazna[int(k/3)][0] + 5 
                            #print(profe[red1[k][0]], grupe[red1[k][1]], "profe 3 casa zaredom",red1[k][2], i,k/3 )
                        else:
                            if red1[k][0] == red2[k+1][0] or red2[k+1][0] == red1[k+2][0] or red1[k+1][0]==red2[k+2][0]  or red2[k][0] == red1[k+1][0]: 
                                #print("profe zarednom", red1[k])  #profe imaju zaredom 2 casa, bitno upratiti sve 4 kombinacije                                                     
                                kazna[int(k/3)][0] = kazna[int(k/3)][0] + 1
                                #print(profe[red1[k][0]], grupe[red1[k][1]], "profe 2 casa zaredom",red1[k][2], i,k/3 )     

                        if red1[k][1] == red2[k+2][1]: #studenti imaju ili pauzu ili 3 casa zaredom                  
                            if red1[k][1] in provjera[int(k/3)]:
                                kazna[int(k/3)][1] = kazna[int(k/3)][1] + 1
                                #print(profe[red1[k][0]], grupe[red1[k][1]], "studenti 3 casa zaredom ",red1[k][2], i,k/3 )
                            else: 
                                kazna[int(k/3)][2] = kazna[int(k/3)][2] + 2.5
                                #print(profe[red1[k][0]], grupe[red1[k][1]], "studenti 2 + pauza",red1[k][2], i,k/3 )
                                
        suma = 0 #kaznee u vrijednost pretvaramo
        for i in kazna:
            suma = suma + sum(i) 
        #ppomnoziti sa -1
        self.fitness = -suma + vrijednost
        #print(self.preklapanja)
        #print("problem1", self.problem1, "problem2", self.problem2)
        return self.fitness


    def Ispisi_raspored(self, imena_profa=False, imena_grupa=False):
        br=0
        headers = ["PON", "UTO", "SRI", "CET", "PET"]
        derp = copy.deepcopy(self.hromozom)
        if (imena_profa==True or imena_grupa==True):
            for i in derp:
                for j in i:
                    if (imena_profa==True):
                        j[0] = profe[j[0]]
                    if (imena_grupa==True):
                        j[1] = grupe[j[1]]
        for i in derp:
            x=[]
            x.append(i[0::3])
            x.append(i[1::3])
            x.append(i[2::3])
            print("\n\n")
            print'                            ------------ sala', br,'------------'
            br = br +1
            print(tabulate(x,headers,tablefmt="grid")) #samo promijeniti latex umjesto grid za latex table
        

class Populacija:
    def __init__(self, v_pop1, v_elite1, max_gen1):
        self.vel_pop = v_pop1
        self.vel_elite = v_elite1
        self.max_br_gen = max_gen1

        #self.predmeti=list([[1,2,"PAI"], [4,3,"SREES"], [1,3,"PA/PE"], [2,2,"LSAU"], [2,3,"DSU"], [5,3,"SIS"], [5,3,"PLS"], [3,1,"LAG"],[0,0,"PAUZA"], [0,0,"PAUZA"], [0,0,"PAUZA"]])
        #self.predmeti=list([[1,2,"PAI"], [4,3,"SREES"], [1,3,"PA/PE"],           [2,2,"LSAU"], [2,3,"DSU"], [5,2,"SIS"],               [5,3,"PLS"], [3,1,"LAG"], [1,3,"PA"],            [1,4,"OR"], [4,3,"EES"], [2,4,"NSAU"],              [2,4,"LSAU2"], [2,4,"DSU2"], [5,4,"SIS2"], 
        #                   [5,3,"PLS2"], [3,2,"LAG2"], [1,3,"PAI2"],            [4,4,"SRgS3"], [1,4,"PA2"], [1,6,"OR5"],              [4,6,"ES5"], [2,6,"AU5"], [1,7,"O6"],            [4,7,"S6"], [2,7,"U6"], [1,2,"PAI6"],                [4,3,"SREES6"], [1,3,"PA/PE6"], [2,2,"LSAU7"]])
        
        
        self.predmeti = list([[10, 2, "AE"], [11, 2, "SIM"], [12, 2, "EMJ"], [14, 2, "IM3"], [15, 2, "EK2"], [7, 2, "DM"], [8, 2, "DS2"], [16, 2, "LSAU"], [6, 2, "DE"], [17, 2, "MIS"], [18, 2, "AKT"], [19, 2, "OPTO"], [20, 2, "OAD"], [21, 2, "PAI"], [10, 2, "PEE"], [22, 3, "SIS"], [22, 3, "PLS"], [16, 3, "DSU"], [23, 3, "DIK"], [21, 3, "PA"], [10, 3, "PE"], [6, 3, "OEE"], [20, 3, "RPR"], [24, 3, "SRES"], [22, 3, "PMS"], [17, 3, "ROB"], [18, 3, "MEH"], [25, 3, "DFTS"], [16, 4, "NSAU"], [26, 4, "DOS"], [27, 4, "DRAOS"], [21, 4, "OR"], [28, 4, "MMS"], [18, 4, "DS4"], [27, 4, "BSS"], [10, 4, "NEKS"], [21, 4, "OU"], [8, 4, "PIP"], [17, 4, "IS"], [29, 4, "OII"], [7, 12, "NA"], [7, 12, "DMri"], [30, 12, "LD"], [31, 12, "OBP"], [28, 12, "ASP"], [30, 12, "RA"], [20, 12, "OOAD"], [28, 12, "AFJ"], [32, 12, "RMA"], [21, 12, "US"], [33, 12, "ORM"], [34, 12, "DSP"], [38, 12, "CCI"], [39, 12, "IEK"], [29, 13, "OOI"], [35, 13, "OIS"], [32, 13, "WT"], [9, 13, "PJP"], [30, 13, "SI"], [36, 13, "VI"], [37, 13, "ARM"],[31, 14, "BP"], [30, 14, "PRS"], [48, 14, "POOS"], [29, 14, "OI"], [37, 14, "RM"], [35, 14, "PPIS"], [49, 14, "NGA"], [48, 14, "NSSI"],[40, 22, "PEES"], [41, 22, "IE"], [15, 22, "OES"], [42, 22, "EMJ2"],[5, 22, "EMAT"], [39, 22, "IEEK"], [16, 22, "OSAU"], [43, 22, "OMEH"], [11, 22, "SIP"],[40, 23, "TVNI"], [44, 23, "ES"], [41, 23, "PEE1"], [45, 23, "ELMS"], [46, 23, "TVI"], [47, 23, "EISM"],[47, 23, "ESIT"], [47, 23, "ESP"], [47, 23, "EPOS"], [25, 23, "EPOG"], [45, 23, "PREE"], [44, 23, "UPEE"]])
        self.populacija=[] #lista objekata tipa raspored

        self.suma_RWS = 0 #potrebno za RWS

        self.nadjeno_opt_rj = False #potrebno za raniji prekid petlje
        self.lista_rj = [] #potrebno za plotanje liste rjesenja
    
    def Get_populacija(self):
        return self.populacija

    def Generisi_pocetnu_populaciju(self):
        for i in range(self.vel_pop):
            random.shuffle(self.predmeti)
            jedinka = Raspored()
            jedinka.hromozom=[]
            jedinka.hromozom.append( list(self.predmeti[0:15]) ) #ovdje ide od 0:15 posto imamo 15 termina po sali sedmicno, 3ter x 5 dana
            jedinka.hromozom.append( list(self.predmeti[15:30]) ) #ovdje takodjer
            jedinka.hromozom.append( list(self.predmeti[30:45]) )
            jedinka.hromozom.append( list(self.predmeti[45:60]) )
            jedinka.hromozom.append( list(self.predmeti[60:75]) )
            jedinka.hromozom.append( list(self.predmeti[75:90]) )
            jedinka.Evaluiraj_fitness()
            #ovdje treba appendati n puta, gdje je n broj sala, da se skontati logika da se unutar petlje
            self.populacija.append(jedinka)
            random.shuffle(self.predmeti)
    
    def Ispisi_populaciju(self):
        for i in self.populacija:
            i.Ispisi_raspored()
        

    def Sortiraj_populaciju(self):
        self.populacija.sort( key=Raspored.Get_fitness, reverse=True)
        #kriteriji je fitness! trebat ce azurirati ovo! sortira u opadajuci poredak
    
    def Nadji_sumu_RWS(self):
        self.suma_RWS = 0
        for i in self.populacija:
            self.suma_RWS = self.suma_RWS + i.Get_fitness()
        
    def Odaberi_indeks_RWS(self):
        j = 0
        random.shuffle(self.populacija)
        suma = self.populacija[0].Get_fitness() / self.suma_RWS
        u = random.uniform(0,1)
        while suma < u:
            j = j + 1
            if (j >= len(self.populacija) ):
                return j-1
            suma = suma + self.populacija[j].Get_fitness() / self.suma_RWS
        return j

    def Nova_generacija(self):
        nova_gen = []

        #prvih vel_elite uzimamo automatski
        self.Sortiraj_populaciju()
        #print"Najbolje rjesenje ove generacije je raspored sa fitnessom==", self.populacija[0].Get_fitness()
        self.lista_rj.append( self.populacija[0].Get_fitness())
        if ( self.populacija[0].Get_fitness() >= 0 ):
            self.nadjeno_opt_rj = True
        for i in range(self.vel_elite):
            x = copy.deepcopy(self.populacija[0])
            nova_gen.append(x)
            #zatim ubacimo i po dvije mutacije od najboljih
            y = self.Mutacija_druga(copy.deepcopy(self.populacija[0]) )
            nova_gen.append(y)
            z = self.Mutacija_cetvrta(copy.deepcopy(self.populacija[0]) )
            nova_gen.append(z)
            del self.populacija[0]

        #sada nam treba jos vel_pop - 3*vel_elite jedinki, selektujemo ih preko RWS
        indeksi = []
        self.Nadji_sumu_RWS()
        for i in range(self.vel_pop - self.vel_elite * 3):
            indeksi.append(self.Odaberi_indeks_RWS())
        
        #mutiranje selektovanih jedinki
        for i in indeksi:
            koja_mut = random.randint(1,4)
            x = copy.deepcopy(self.populacija[i])
            if koja_mut==1:
                nova_gen.append(self.Mutacija_druga(x))
            elif koja_mut==2:
                nova_gen.append(self.Mutacija_druga(x))
            elif koja_mut==3:
                nova_gen.append(self.Mutacija_cetvrta(x))
            else:
                nova_gen.append(self.Mutacija_cetvrta(x))
        for i in nova_gen:
            i.Evaluiraj_fitness()
        self.populacija=nova_gen


    def Sprovedi_pretragu(self):
        for i in range(self.max_br_gen):
            #print"------------------ generacija ", i+1, " ----------------------"
            #for j in self.populacija:
            #    print j.Get_fitness()
            self.Nova_generacija()
            if self.nadjeno_opt_rj == True:
                break
        self.Sortiraj_populaciju()
        print "RJESENJE:", self.populacija[0].Get_fitness()
        self.populacija[0].Ispisi_raspored(True,True)

    
    #--Mutacija_prva---zamjena 2 casa koji prave problem
    #--Mutacija_druga---zamjena 2 random casa
    #--Mutacija_treca---izmiksamo predmete od 2 dana koja najvise problema prave
    #--Mutacija_cetvrta---izmiksamo predmente od 2 random dana--rijesen problem i kada miksamo predmete od istog dana
    def Mutacija_prva(self, kemina_jedinka, problem1=[], problem2=[]):
        jedinka=kemina_jedinka
        if len(problem1)==0 and len(problem2)==0:
            problem1=jedinka.problem1
            problem2=jedinka.problem2
        jedinka.hromozom[problem1[0]][problem1[1]], jedinka.hromozom[problem2[0]][problem2[1]]=jedinka.hromozom[problem2[0]][problem2[1]], jedinka.hromozom[problem1[0]][problem1[1]]
        #print("zamjena", jedinka.hromozom[problem2[0]][problem2[1]], jedinka.hromozom[problem1[0]][problem1[1]])
        return jedinka

    def Mutacija_druga(self, jedinka):
        problem1=[random.randint(0,len(jedinka.hromozom)-1), random.randint(0,14)]
        problem2=[random.randint(0,len(jedinka.hromozom)-1), random.randint(0,14)]
        return self.Mutacija_prva(jedinka, problem1, problem2)

    def Mutacija_treca(self, jedinka, index1=0, index2=0):
        if index1 ==0 and index2 == 0:
            index1, value1 = max(enumerate(jedinka.preklapanja), key=operator.itemgetter(1))
            #print("indeks i vrijednost", index1,value1)
            jedinka.preklapanja[index1]=-1
            index2, value2 = max(enumerate(jedinka.preklapanja), key=operator.itemgetter(1))
            jedinka.preklapanja[index1]=value1
        skup=[]
        #print("dan", index1+1, index2+1)
        for i in range( len(jedinka.hromozom) ):
            skup.append( jedinka.hromozom[i][3*index1] )
            skup.append( jedinka.hromozom[i][3*index1+1] )
            skup.append( jedinka.hromozom[i][3*index1+2] )
            if (index1 != index2): #da bi obezbijedili da ne dodje do gubitaka predmeta, bitno
                skup.append(jedinka.hromozom[i][3*index2])
                skup.append( jedinka.hromozom[i][3*index2+1] )
                skup.append( jedinka.hromozom[i][3*index2+2] )
        
        random.shuffle(skup) #miks miks miks
        j=0
        for i in range(len(jedinka.hromozom)):
            #print(j)
            jedinka.hromozom[i][3*index1], jedinka.hromozom[i][3*index1+1], jedinka.hromozom[i][3*index1+2]=skup[j], skup[j+1], skup[j+2]
            
            if index1 != index2:
                jedinka.hromozom[i][3*index2], jedinka.hromozom[i][3*index2+1], jedinka.hromozom[i][3*index2+2]=skup[j+len(skup)/2], skup[j+1+len(skup)/2], skup[j+2+len(skup)/2]
            
            j=j+3
        return jedinka
    
    def Mutacija_cetvrta(self, jedinka):
        index1=random.randint(0,4)
        index2=random.randint(0,4)#ako su index1 i index2 isti dolazi do miksanja predmeta u jednom danu
        return self.Mutacija_treca(jedinka, index1, index2)
    
    def Plottaj(self):
        plt.figure()
        n=[]
        for i in range(len(self.lista_rj)):
            n.append(i)
        plt.plot(n, self.lista_rj)
        plt.xlabel('Generacija')
        plt.ylabel('Fitness')
        plt.show()


def main():
    x = Populacija(180,12,800)
    x.Generisi_pocetnu_populaciju()
    start = time.time()
    x.Sprovedi_pretragu()
    end = time.time()
    print "Vrijeme izvrsavanja u sekundama je =", end-start, "sekundi."
    x.Plottaj()

main()