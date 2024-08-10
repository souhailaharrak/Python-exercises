"""def facterielle(n):
    if n==0 or n==1:
        return 1
    f=1
    for x in range(2,n+1):
      f=f*x
    return f
print(facterielle(4))"""

"""def compte_voyelle(ch):
     ch=ch.lower()
     voyelle="AEIUOaeiuo"
     count=0
     for i in ch:
      if i in ch:
            count+=1
     return count
print(compte_voyelle("souhila")) """

"""def est_palindrome():
    ch=input("entre une chaine de character ")
    ch=ch.lower()
    ch=ch.replace(" ","")
    if ch==ch[::-1]:
      return True
    else:
        return False
    
print(est_palindrome())"""

"""def  conversion_temperatures(Celsius):
    f= (Celsius * 9)/(5 + 32)
    return f
print(conversion_temperatures(5))"""

"""f=lambda x:x*2
print(f(2))"""

"""f=lambda a,b:a+b
print(f(2,4))"""
"""con=lambda a,b:a+" "+b
print(con("dsds","sdsd"))"""

def ajouter_tuples(t1,t2):
  if len(t1)!=len(t2):
        raise ValueError("ne pas la meme longueur")
  somme=tuple()
  for i in range(len(t1)):
        somme+=(t1[i]+t2[i],)
  return somme
t1=(1,3,2,3)
t2=(1,3,2,3)
print(ajouter_tuples(t1,t2))
    