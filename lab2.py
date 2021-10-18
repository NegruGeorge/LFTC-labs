f = open("input.py","r")

# for line in f:
#     print(len(line))
#     for s in line:
#         print(s =="\n")
#         print(s==" ")
#     break


def cuvantRezervat(cuv):
    
    if(cuv =="**" or cuv == "<=" or cuv ==">=" or cuv =="==" or cuv == "!="):
        # print(cuv + "?/////////////////////")
        return True
    return False



def printAtomi1(file:str):
    for line in file:
        atom = ""
        cuvRez=0
        ghilimele = 0
        for s in line:
            # matcheaza inceput de string
            if(s=='"'):
                ghilimele+=1

            if(ghilimele!=0):
                # verifica ce a fost inainte de string si afiseaza
                # verifica daca urmatorul caracter e " adica daca incepe un string, daca da atunci afiseaza atomul de inainte
                if(s=='"' and ghilimele==1):
                    print(atom)
                    atom=""
            elif s in " !():,*-+/%**><>=<=\n" :
                # in caz ca am un cuvant rezervat (>=  != ) imi returneaza true si merge mai departe pentru a l cauta 
                if cuvantRezervat(atom + s): 
                    cuvRez=1
                # in caz ca nu e cuvant rezervat si urmatorul caracter se afla in multimea de mai sus
                # afisam atomul ce era inainte gasit (daca acesta e diferit de "")
                elif len(atom) !=0:
                    print(atom)
                
                if cuvRez!=1:
                    atom=""
                cuvRez=0
            
            # aici verificam daca cumva atom ul era cuvant din multimea respectiva sau cuvant rezervat 
            # daca era atunci il afisam
            elif (len(atom)!=0 and atom in " !():,*-+/%**><>=<=\n") or cuvantRezervat(atom):
                print(atom)
                atom =""

            if(s!=" "):
                atom+=s
            if(s==" " and ghilimele!=0):
                atom+=s

            if(ghilimele==2):
                ghilimele=0
            

printAtomi1(f)

#paranteza trebuie afisata goala 


