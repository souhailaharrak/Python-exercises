thisdic={"name":"souhaila","age":11,"sex":"fem"}
print(thisdic)
x=thisdic.get("name") #return dun valeur
#modifier dun vealur
#x=thisdic["name"]="pyhthon"
#print(x)                                                  

#ajouter des keys
#y=thisdic["color"]="blue"
#print(thisdic)
 
#parcour les cles et les valeurs 
#for x,y in thisdic.items():
#     print(x,y).


#check
#if "nae" in thisdic:     
 #   print("yes")

#del (thisdic)
#print(thisdic)

#supp un elemet specifque use pop
#thisdic.pop("name")
#print(thisdic)
 #copy une dic
#x=thisdic.copy()
#print(x)

############################

etudiant={"nom":"souhaila","prenom":"harrak","ville":"paris"}
#nom=etudiant["nom"] #acces une cle 
#print(nom)
#age=etudiant.get("age",22)
#print(age)
#n=etudiant["ville"]="marroc" #modifier 
#print(etudiant)
#a=etudiant["adress"]={"reu":"so"}
#print(etudiant)
for i in etudiant:
    print(f"{i} : {etudiant[i]}")
    
 ###############################EXRCISES   
"""j={"nom":"CR7","Prenom":"c","position":"attaque","prix":55000,"nom_equipe":"Psg"}
j1={"nom":"neymar","Prenom":"jn","position":"attaque","prix":55000,"nom_equipe":"Psg"}
if j["nom_equipe"]==j1["nom_equipe"]:
   print(f"{j['nom']} est la meme equipe de {j1['nom']}")
else:
       print(f"{j['nom']} nest pas la meme equipe de {j1['nom']}")
"""

s1={"nom":"souhaila","prenom":"harrak","professeur":"M.Bellaj","numéro d’inscription":1111,"pr":{"son numéro de somme":1200,"nom":"M.Bellaj","prénom":"mohammed","diplôme":"Bac+5","année de recrutemente":2014,"spécialité":"informatique"}}
s2={"nom":"houda","prenom":"bedu","professeur":"M.Bellaj","numéro d’inscription":12121,"pr":{"son numéro de somme":120,"nom":"M.Bellaj","prénom":"mohammed","diplôme":"Bac+5","année de recrutemente":2024,"spécialité":"informatique"}}
#if s1["pr"]["son numéro de somme"]==s2["pr"]["son numéro de somme"]:
 #  print(f"{s1['nom']} est la meme profeesur de {s2['nom']}")
#else:
    
 #  print(f"{s1['nom']} est ne pas meme profeesur de {s2['nom']}")

if s1["pr"]["année de recrutemente"]<s2["pr"]["année de recrutemente"]:
    
    print(f"{s1['nom']} il a un proffesur ancien de stagier {s2['nom']}")
else:
        print(f"{s2['nom']} il a un proffesur ancien de stagier {s1['nom']}")

    
    
  


def enregestrie_voiture(nbr_voitures):
    voitures=[]
    for i in range(nbr_voitures):
        matricule=int(input("entre votre matricule "))
        #marque=input("entre votre marque ")
        #modèle=int(input("entre votre modèle "))
        prix=int(input("entre votre prix "))
        voiture={
            "matricule":matricule,
           # "marque":marque,
            #"modèle":modèle,
            "prix":prix
            
            }
        voitures.append(voiture)
    return voitures
print(enregestrie_voiture(1))

def voitures_plus_chere(voitures):
    voiture_plus_chere=None
    prix_max=0
    for voiture in voitures:
        if voiture["prix"] > prix_max:
            prix_max=voiture["prix"]
            voitures_plus_chere=voiture
    return voitures_plus_chere
voitures=enregestrie_voiture(3)
voiture_plus_chere=voitures_plus_chere(voitures)
print(voiture_plus_chere)
    

    
    
    
    
    