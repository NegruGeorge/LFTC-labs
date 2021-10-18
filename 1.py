#  # -> comentariu
# ID -> string   # un string care ne spune numele variabilei 
# CONST -> numere, string uri
# <functie> -> <antet> <lista_instructiuni>
# <antet> -> def ID (<lista_parametrii>)  : | def ID () :
# <lista_parametrii> -> <parametru>, <lista_parametrii> | <parametru>
#<lista_parametrii> ->  <empty>
# <empty> ->
# <parametru> -> ID: <tip>
# <lista_instructiuni> -> <instructiune>,<lista_instructiuni> | <instructiune>
# <instructiune>-> <instructiune_if(selectie)>| <instructiune_if_else(selectie)>  | < instructiune_repetitiva(ciclare)>  | <instructiune_return>
#<lista_instructiuni>-> 

#<instructiune_return> -> return ID | CONST

#<instructiune_if(selectie)>-> if  <conditie>: <listainstructiuni>

#<instructiune_if_else(selectie)>-> if  <conditie>: <listainstructiuni> else: <listainstructiuni>

#<instructiune_repetitiva(ciclare)-> while(<conditie>) {<listainstructiuni>}

#<conditie> -> :ID <operator> <conditie> | CONST <operator> <conditie>
# (ID)->  null | ID  # ( optional)
#<operator> ->  > | < | >= | <= | == | or | and | != | / | * | % | + | - | **
#<conditie>->
# <Atribuire>: ID:<tip> =  CONST | ID:<tip> = ID |  ID:<tip> = <operatie>
# <intrare/iesire> -> input(<tip>) / print(<tip>)
# <operatie> ->   | ID <operatie> ID | ID <operatie> CONST | CONST <operatie> ID | CONST <operatie> CONST
# int(<tip>) ->  tip = int   #transform un tip in int

# <Tip compus>: class <ID>: <atribute_tip_compus> <functie>  
#<functie> empty
#<atribute_tip_compus>-> <Atribuire>


# operand -> fara repetitie

#  tip de date de utilizator  ( clasa etc )
#////////////////////////////////////////


# calculeaza perimetrul si aria cercului de o raza data data

def perimetru_aria(raza:float):
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


#err 1
# if 2===3:
#     print("da")




# err1
def test():
    i:int = 10
# eroarea 1, nu am -= in limbajul meu dar merge in python
    i-=1
    print(i)

#i++;
#i--;


#eroarea 2, nu exista for in limbajul meu dar in python
def test3():
    for i in range(0,10):
        print(i)


# nu merge python

# def test1():
#     i:int = 10
#     i++;

# def test2():
#     i:int = 10
#     i--;