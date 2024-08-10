"""a:lambda x,y:x+y
print("souhaila","harrak")"""
n=int(input("entre votre number "))

#facterielle
def facterielle():
    if n==1 or n==0:
        return 1
    f=1
    for i in range(2,n+1):
        f *=i
    return f
f=facterielle()
print(f)

#
def plandrom(n):
    chain=n.replace(" ","")
    chain=n.lower()
    if n==n[::-1]:
      return True
    else:
        return False
r="ree fr"
print(plandrom(r))

#def compte_voyelle():
    n=input("entre une phrase ")
    v="aiuoy"
    n=n.lower()
    count=0
    for chain in n:
     if chain in v :
       count +=1
    
    return count
count=compte_voyelle()
print(count)





