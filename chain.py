"""chain=input("entrez une phrase ")
sous_chain=input("entre une sous chain ")
nouvelle=input("entre la nouvelle chain")
res=chain.replace(sous_chain,nouvelle)
print(res)"""

"""chain=input("entre une phrase ")
res=" Bonjour " + chain + "!"
print(res)"""

"""phrase=input("entre votre chain ")
s=phrase.replace(" ","")
print(s)"""

"""phrase=input("entre votre chain ")
s=phrase.replace("a","@")
print(s)"""

"""chain=input("entre des phrases ")
if chain.isupper():
    res=chain.lower()
elif chain.islower():
    res=chain.upper()
else:
    res=chain
print(res)"""

"""chain=input("entre des phrases ")
voyelle ="AUOIEaioue"

for i in chain:
    if i not in voyelle:
        print(i)
"""
"""phrase = input("Entre : ")
mots=phrase.split()
inverse = mots[::-1]
res = "#".join(inverse)
print(res)"""

"""nom=input("entre votre nom")
age=int(input("entre votre age"))
res=f"bonjour {nom} ,vous avez {age} ans "
print(res)"""

"""chain=input("entre votre phrase ")
chain=chain.lower()
if chain==chain[::-1]:
   print(chain)t
else:
    print("Non ne pas plandrome")"""

phrase=input("entre votre phrase ")
res=phrase[-1]+phrase[1:-1]+phrase[0]
print(res)
    

