def perimetru_aria(raza:float):
    class ceva:
        x:int =1
    
    perimetru:float = 2*3.14*raza
    print(perimetru)
    
    aria:float = 3.14* raza**2
    print(aria)

def cmmdc(nr1:int,nr2:int):
    while(nr1!=nr2):
        if nr1>nr2:
            nr1 = nr1-nr2
        else:
            nr2 = nr2-nr1

    print(nr1)

def suma_n_nr():
    n:int = input("introduceti nr de numere pe care doriti sa le cititi de la tastatura: \n")
    suma:int = 0
    n = int(n)
    while(n):
        nr:str = input("introduceti un nr: \n")
        numar = int(nr)
        suma = suma+ numar
        n=n-1
    print(suma)


perimetru_aria(10)
cmmdc(15,10)

suma_n_nr()
