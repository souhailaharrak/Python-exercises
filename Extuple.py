mon_tuple=(1,2,3)
"""print(len(mon_tuple))
r=mon_tuple[0]
r=mon_tuple[-1]"""
y=list(mon_tuple)
y[0]= 5
mon_tuple=tuple(y)
"""print(mon_tuple)"""
last_tuple=(4,5,6)
nouveau_tuple=last_tuple+mon_tuple
print(nouveau_tuple)


"""if 5 in nouveau_tuple:
    print("yes")
else:
        print("non ")"""

"""for x in nouveau_tuple:
    print(x)"""



def ajouter_tuple(tuple1,tuple2):
    if len(tuple1) == len(tuple2):
        
      resultat=tuple()
      for i in range(len(tuple1)):
        resultat +=(tuple1[i]+tuple2[i],)
      return resultat
tuple1=(1,3,4)
tuple2=(4,5,6)
res=ajouter_tuple(tuple1,tuple2)
print(res)

