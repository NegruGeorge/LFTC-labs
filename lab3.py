f = open("input.py","r")


codAtom_program ={}
codAtom_variabile={}
indexAtom_program=1
indexAtom_variabile=1

listaCuvinteProgram = ["def","if","else","in","input","print","while","float","int","str","return"]

def cuvantRezervat(cuv):
    if(cuv =="**" or cuv == "<=" or cuv ==">=" or cuv =="==" or cuv == "!="):
        return True
    return False





def check_cuvinte_program(atom):
    global indexAtom_program
    global indexAtom_variabile

    if(cuvantRezervat(atom) or  (atom in " !():,*-+/%**><>=<=\n") or  (atom in listaCuvinteProgram)):
        if(atom not in codAtom_program):
            codAtom_program[atom]=indexAtom_program
            indexAtom_program= indexAtom_program+1
        codAtom_variabile[atom] = 0
    else:
        codAtom_program[atom] =0

        if(atom not in codAtom_variabile):
            codAtom_variabile[atom] = indexAtom_variabile
            indexAtom_variabile = indexAtom_variabile+1


def printAtomi1(file:str):
    global indexAtom_program
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
                    check_cuvinte_program(atom)
                    if(len(atom)>8):
                        print(atom + " ->ERROR: length overflow !")
                    else:
                        print(atom + " " +str(codAtom_program[atom]) + " "+ str(codAtom_variabile[atom]))
                    atom=""
            elif s in " !():,*-+/%**><>=<=\n" :
                # in caz ca am un cuvant rezervat (>=  != ) imi returneaza true si merge mai departe pentru a l cauta 
                if cuvantRezervat(atom + s): 
                    cuvRez=1
                # in caz ca nu e cuvant rezervat si urmatorul caracter se afla in multimea de mai sus
                # afisam atomul ce era inainte gasit (daca acesta e diferit de "")
                elif len(atom) !=0:
                    check_cuvinte_program(atom)
                    if(len(atom)>8):
                        print(atom + " ->ERROR: length overflow !")
                    else:
                        print(atom + " " +str(codAtom_program[atom]) + " "+ str(codAtom_variabile[atom]))
                    atom=""
                
                if cuvRez!=1:
                    atom=""
                cuvRez=0
            
            # aici verificam daca cumva atom ul era cuvant din multimea respectiva sau cuvant rezervat 
            # daca era atunci il afisam
            elif (len(atom)!=0 and atom in " !():,*-+/%**><>=<=\n") or cuvantRezervat(atom):
                check_cuvinte_program(atom)
                if(len(atom)>8):
                    print(atom + " ->ERROR: length overflow !")
                else:
                    print(atom + " " +str(codAtom_program[atom]) + " "+ str(codAtom_variabile[atom]))
                atom =""

            if(s!=" "):
                atom+=s
            if(s==" " and ghilimele!=0):
                atom+=s

            if(ghilimele==2):
                ghilimele=0
            

printAtomi1(f)

#paranteza trebuie afisata goala 


