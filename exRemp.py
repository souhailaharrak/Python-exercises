"""s="welcom"
n=input("entre la chaine ")
m=s.replace("welc",n)
print(m)"""

#replace la chaine par cha
"""s=input()
yes=s.replace(" ","")
print(yes)"""

#s=input()
#yes=s.replace("a","@")
#print(yes)

#k=input()
#s=input()
#a=k.replace([ :1],s)
#print(a)

#phrase=input("entre une phrase")
#sous_chaine=input(" entre une sous-chaine a remplace: ")
#neuvelle_chaine=input("la neuvelle chaine ")
#phrase_modifier=phrase.replace(sous_chaine,neuvelle_chaine)
#print(phrase_modifier)

#n=input("entre premier phrase ")
#print("Bonjour ",n , "! ")
 #x : is lower() upper()
"""name=input("entre votre name ")
if name == name.upper() :
     print(name.lower())
elif name == name.lower() :
      print(name.upper())
else :
     print("cette phrase est melenge ")"""


 #x : is lower()
name=input("entre votre name ")
if name.isupper() :
     print(name.lower())
elif name.islower() :
      print(name.upper())
else :
     print("cette phrase est melenge ")