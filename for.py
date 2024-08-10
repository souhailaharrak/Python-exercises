#EX1
"""for i in range(1,101):
    print(i)"""
#**********************************************************
"""number=int(input("entre un  number "))
for i in range(11):
    print(i*number,end=" ")"""
#**********************************************************
"""c=input("Donne un mot")
for i in c:
    print(i,end=" ")"""
#***************************************************
"""n=int(input("donne un nomber "))
for i in range(1,n+1) :
    if i%2 == 0 :
     print(i,end=" ")"""
#****************************************************
#ecrire un programme qui permet  d"entre un nombre et compter le nomber de chiffre
"""n=int(input("donne le nombre "))
cmp=0
while n!=0:
    n=n//10
    cmp=cmp+1
print(cmp,end=" ")"""

#*******************************************************************
"""n=int(input("donne un number "))
cmp=0
while n>0 :
    n=n//2
    cmp=cmp+1
print(cmp)"""
#********************************************************************
#Break
s=0
for i in range(1,9):
    n=int(input("donne moi de notre number "))
    if n<0:
         break
    else:
       
       s=s+i

print(s)

#********************************************************************
#continue

"""s=0
for i in range(1,9):
    n=int(input("donne moi de notre number "))
    if n<0:
         continue
    else:
       
       s=s+n

print(s)"""
