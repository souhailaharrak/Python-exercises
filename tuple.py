"""def tup(a,b): 
    t=a+b
    return t
a=(5,6,7,4)
b=(4,6,4,6,234,4)

print(tup(a,b))"""

"""def communs_tuples(a,b):
   return tuple(set(a) & set(b))
a=(5,6,7,4.8,"sss",4)
b=(4,6,4,6,4.8,234)   
res=communs_tuples(a,b)
print(res)"""

"""def occurrences(b): 
 1  2 2 5
 1:1 2 :2
 lista={}
 for i in b:
    if i in lista:
        lista[i] +=1
    else:
        lista[i] =1
 return lista
b=(4,6,4,6,234,4)

print(occurrences(b))"""


"""def rever(): 
 b=(4,6,4,6,234,1)
 b=tuple(reversed(b))
 return b


print(rever())"""

"""def impaire_paire(l):
    
    paire=tuple(num for num in l if num % 2 ==0 )
    impaire=tuple(num for num in l if num % 2 !=0 )
    return paire,impaire
l=[1,3,5,3,4]

print(impaire_paire(l))"""

def convirter(t):
 
    y=list(t)
    y=33
    t=tuple(y)
    return y
t=(4,5,67,4,567,4)
print(convirter(t))
     