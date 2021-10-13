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
            if(s=='"'):
                ghilimele+=1

            if(ghilimele!=0):
                if(s=='"' and ghilimele==1):
                    print(atom)
                    atom=""
            elif s in " !():,*-+/%**><>=<=\n" :
                if cuvantRezervat(atom + s): 
                    cuvRez=1
                elif len(atom) !=0:
                    print(atom)
                
                if cuvRez!=1:
                    atom=""
                cuvRez=0
                    

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


