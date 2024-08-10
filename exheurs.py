def convertit():
    t=int(input("entre le tempe "))
    h=t // 3600
    reste=t % 3600
    m=reste // 60
    s=reste % 60
    print(h,"h",m,"min",s,"sec")
convertit()

def signe(a,n):
    
    if a*n>0:
        
        print("la meme ")
    
    else :
        print("ne pas la meme signe")

signe(-3,-2)



n=int(input("entre le number de photocopie "))

if n<10 :
    f=n*0.30
    
elif n<30 :
    f=10*0.30+(n-10)*0.25
else :
    f=10*0.30+20*0.25+(n-30)*0.20
print(f)



def age( ):
    
    age=int(input("entre votre age "))
    if age>=6 or age <=7 :
        
        print("puissin")
        
    elif age>=8 or age <=9 :
        print("pupille")
    
    elif age>=10 or age <=11 :
        print("minim")
    
    else:
         print("cadet")

age(  )



def notes( ):
    
    note=int(input("entre votre age 1 "))
    note1=int(input("entre votre age2 "))
    note2=int(input("entre votre age3 "))
    moy=(note+note1+note2)/3
    
    if moy>=16:
        print("TB")
        
    elif moy>=14 and moy <16 :
        print("bien")
    
    elif moy>=12 and moy <14 :
        print("assez bien")
    
    elif moy>=10 and moy <12 :
        print("passable ")
    else :
         print("insuffisant")
notes(  )

