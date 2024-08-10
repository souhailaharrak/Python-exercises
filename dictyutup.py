#Python Série Exercices | Les Dictionnaires
etudiants={
    "etudiant1":13,"etudiant2":3,"etudiant3":9.4,"etudiant4":10,"etudiant5":12,"etudiant6":12,"etudiant7":13,
    "etudiant8":15,"etudiant9":19,"etudiant10":13,"etudiant11":8

    }
etudiantAdmis=[]
etudiantNonAdmis=[]

for i,j in etudiants.items():
    if j >=10:
      etudiantAdmis.append(i)    
    
    else:
     etudiantNonAdmis.append(i)
     
     
print(" les etudiant admis ",etudiantAdmis)
print("  les etudiant non  admis ",etudiantNonAdmis)

notes={"souhaila":[17,19,17],"soumia":[16,18,18],"akram":[20,20,19.50]}
newDic={}
for key,value in notes.items():
    sum=0
    for v in value:
        sum +=v
        
    moy=sum/len(value)
    newDic[key]=moy
print(newDic)



##
edt1={ 
        "moyenne":float(input("entreZ les moyenne "))}

##
edt2={  
        "moyenne":float(input("entreZ les moyenne "))}

##
edt3={  
        "moyenne":float(input("entreZ les moyenne "))}

"""
def verfier():
    if edt1["class"]==edt2["class"]==edt3["class"]:
        print("la meme classs")
    else:
        print("ne pas la meme class")
verfier()
"""
if edt1["moyenne"]>edt2["moyenne"] and edt1["moyenne"]>edt3["moyenne"]:
    print(edt1)
elif edt2["moyenne"]>edt1["moyenne"] and edt2["moyenne"]>edt3["moyenne"]:
    print(edt2)
else:
    print(edt3)