from random import *
inimesed = ["A", "B", "C", "D", "E"]
palgad = [1200,2500,750,395,1200]
def sisesta_andmed(i, p):
    """Lisame kasutajat nimekirjasse ja palka
    """
    N = 1
    for n in range(N):
        inimene = input("Sisestage nime: ")
        i.append(inimene)
        palk=int(input("Sisestage palk: "))
        p.append(palk)
    return i,p
def andmed_ekranile(i, p):
    """Näita inimeste nimekiri ja palgad
    """
    N=len(i)
    for n in range(N):
        print(f"{i[n]} - {p[n]}")
def kustutamine(i, p):
    """Isiku nime ja palga eemaldamine nimekirjast
    """
    nimi=input("Sisestage inimese nimi, mida soovite eemaldada: ")
    n=i.count(nimi)
    abi_list=[]
    if n > 0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e))
                print(f"{t}.{i[e]} - {p[e]}")
        j=int(input("Isiku seerianumber: "))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p
def maksimum(i, p):
    """Kasutaja maksimumpalga kuvamine ekraanil olevast nimekirjast
    """
    max_palk = palgad[0] 
    kellel = inimesed[0]
    for p in palgad:
        if p > max_palk:
            max_palk = p
            i = palgad.index(max_palk)
            kellel = inimesed[i]
    print(f"Maksimaalne palk - {max_palk} saab - {kellel}")
def minimum(i, p):
    """Kasutaja miinimumpalga kuvamine loendist ekraanile
    """
    min_palk = palgad[0]
    kellel = inimesed[0]
    for p in palgad:
        if p < min_palk:
            min_palk = p
            i = palgad.index(min_palk)
            kellel = inimesed[i]
    print(f"Minimaalne palk - {min_palk} saab - {kellel}.")