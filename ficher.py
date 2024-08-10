#f=open(r"C:\Users\Zak\OneDrive\Desktop\m.txt", "r")
 

#print(f.read())
#print(f.readline(2))           
#c=0
#for x in f :
 #   print(x)
  #  c+=1
#print(c)
#f.close()
#f=open(r"C:\Users\Zak\OneDrive\Desktop\m.txt", "a")
#f.write(" harrak souhaila")           
#f.close()                  

#f=open(r"C:\Users\Zak\OneDrive\Desktop\m.txt","r")
#print(f.read())
  
  
#ecrivz le contenu du ficher txtor a la suit du ficher txtcopi  
#origine=open(r"C:\Users\Zak\OneDrive\Desktop\txtorigine.txt", "a")
#copie=open(r"C:\Users\Zak\OneDrive\Desktop\txtcopie.txt","r")
#txt=copie.read()
#origine.write(txt)
#print(txt)
#copie.close()
#origine.close()
  
#b f=open(r"C:\Users\Zak\OneDrive\Desktop\exf5.txt", "a")
#f=open(r"C:\Users\Zak\OneDrive\Desktop\exf5.txt", "r")
#print(f.read())
#f.close()

#f.write(" halloe")
#f=open(r"C:\Users\Zak\OneDrive\Desktop\exf5.txt", "r")

#print(f.read())
#f.close()
  """"
f=open(r"C:\Users\Zak\OneDrive\Desktop\exf5.txt", "w")
f.write("word ")
f.close()
f=open(r"C:\Users\Zak\OneDrive\Desktop\exf5.txt", "r")
print(f.read())"""


#lire un ficher
def red_file(filename):
    with open(filename,"r") as f:
        data=f.read()
        print(data) 
 

#ecrire dans un ficher
def rite_to_file(filename,text):
    with open(filename,"w") as f:
        f.write(text)
rite_to_file(r"C:\Users\Zak\OneDrive\Desktop\exf5.txt","souhila as ")
red_file(r"C:\Users\Zak\OneDrive\Desktop\exf5.txt")



#copier le contenu d"un ficher dans un autre
def copy_file(source_file, destination_file ):
    with open(source_file,"r") as f:
        data=f.read()
    with open(destination_file,"w") as f:
        f.write(data)
copy_file(r"C:\Users\Zak\OneDrive\Desktop\txtorigine.txt",r"C:\Users\Zak\OneDrive\Desktop\txtcopie.txt")




#compter le nomber des motes ans un ficher

def count_words(filename):
    with open(filename,"r") as f :
        text=f.read()
        words=text.split()
        return len(words)
num_word=count_words(r"C:\Users\Zak\OneDrive\Desktop\exf5.txt")
print(f"{num_word}")



#compter le nomber de ligne dans un ficher
def comp_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return len(lines)

num_lines = comp_lines(r"C:\Users\Zak\OneDrive\Desktop\exf5.txt")
print(f"Nombre de lignes : {num_lines}")



#calcule averge

"""def calulate_average(file_path,column_name):
    total=0
    count=0
    with open(file_path, mode="r") as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            total +=int(row[column_name])
            count +=1
        average=total/count if count>0 else 0
        print(f"averge {column_name} :{average}")
calulate_average(r"C:\Users\Zak\OneDrive\Desktop\ExercicesPy\‪add.csv","age")"""



