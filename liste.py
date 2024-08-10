def somme_list(lista):
    s=0
    
    for i in lista:
       s= s+i
    return s
liste=[1,5,12,56]
print(somme_list(liste))

def iverse_liste():
    lista=[1,2,4,3]
    for x in lista:
        k=lista[::-1]
    return k
print(iverse_liste())

def iverse_liste(lista):
    return lista[::-1]
lista=(1,4,2)    
res=iverse_liste(lista)
print(res)
def iverse_liste():
    lista=[1,2,4,3]
   
    lista.reverse()
    return lista
   
print(iverse_liste())

def double(lista):
    listd=[]
    for x in lista:
        if x not in listd:
            listd.append(x)
    return listd
print(double(lista=[1,3,5,4,1,2,99]))

def concatener_listes(list2,list1):
     return list2+list1
list1=[1,3,5,3]
list2=[1,22,5,3]
     
print(concatener_listes(list2,list1))


#**************************************************************************
n=int(input("entre une number positif "))
l=[]
while n<1 :
    n=int(input("entre une number positif "))

"""for i in range(1,n+1):

     l.append(i)
print(l)"""

for i in range(1,n+1):
  if (i % 2==0 ):
     l.append(i)
print(l)