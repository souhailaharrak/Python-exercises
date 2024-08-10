#suppermer le voyelle
"""mot=input("entre une phrase ")
voyelle="auieyAUIYE"

#concatener
ch=",".join(chain for chain in mot if chain not in  voyelle)

print(ch)"""


#split  use dans tableAU delete sypbolre (inverse de join_)  [d:f]
#echange la premier et le dernier lettre condition 
"""mot=input("entre une phrase ")
if len(mot)>=2 :
 print(mot[-1]+ mot[1:-1] +mot[0])
else:
    print("le mot doit etre au moit deux carachrter ")"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++S
#somme
"""n=int(input("donne moi de notre number "))
s=0
for i in range(1,n+1):     
       s=s+i

"""#print(s)
#****************************************************************S
n=int(input("entre un number "))

for i in range(n+1):
      print(str(i)*i,end=" ")
      
#**********************************************************

s=0
for i in range(1,11):     
       s = s+(i)**2
print(s)









