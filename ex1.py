#EX1 DE PROF ZOU
txt="hello python"
reserve=""
#la longuer de la chaine
p=len(txt)
print(p)
#la nomber de e contient de txt
print(txt.count("e"))
                                                                    
#inverse le phrase
for i in range(p-1,-1,-1):
    reserve +=txt[i]
print(reserve)

#calcul le noumbre de mots
mot=input("donnez une phrase ")
c=len(mot.split())
print(c)

#******************************************************************
#calcul le number de voyalle dans chaine
chaine=input("donne une phrase")
c=0
for i in chaine :
if(i== "a" or i== "o" or i== "i" or i== "u" or i== "y") :
    c=c+1
print("le number de character est : " c)


#*********************************************************
ch3=""
ch1=input("donne une phrase ")
ch2=input("donne une phrase ")
p=len(ch1)
p1=len(ch2)
for i in range(0,int(p//2)):
    ch3=ch3+ch1[i]
for i in range(0,int(p1//2)):
          ch3=ch3+ch2[i]
print(ch3)
#*******************************************************
 #suppremer un character
phrase=""
ch1=input("donnez une phrase")
x=input("donne le character ")

p=len(ch1)
for i in range(0,p):
    if (ch1 !=x) :
        phrase +=ch1[i]
ch1=phrase
print(phrase)
