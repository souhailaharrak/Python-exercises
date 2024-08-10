#ecrire dans un ficher csv
import csv
def write_csv(file_path,data):
    with open(file_path,mode ="w", newline ="") as file:
        fieldnames= data[0].keys()
   S     writer= csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
         writer.writerow(row)
data = [{"nom": "salima", "age":18},{"nom": "souhaila", "age":23},{"nom": "fouad", "age":22},{"nom": "zaka", "age":88},{"nom": "sss", "age":22}]
write_csv("‪df.csv",data)

#lire un ficher
def red_csv(file_path):
    with open(file_path, mode="r") as file:
        csv_read=csv.reader(file)
        for row in csv_read:
            print(row)
red_csv(r"C:\Users\Zak\OneDrive\Desktop\ExercicesPy\‪df.csv")

 


import csv #lecteur deun coloum specifique
with open(r"C:\Users\Zak\OneDrive\Desktop\ExercicesPy\‪df.csv",'r') as f:
     reader=csv.reader(f,delimiter=",")
     print("liste de noms :")
     for row in reader:
         print(row[1])
                      
#lecteur total
with open(r"C:\Users\Zak\OneDrive\Desktop\ExercicesPy\‪df.csv") as f:
     reader=csv.reader(f,delimiter=",")
     print("liste de noms :")
     for row in reader:
         print(row)


import pandas as pd
def merge_CSV(file_path1,file_path2,key):
    #red the csv files
    df1=pd.read_csv(file_path1)
    df2=pd.read_csv(file_path2)
    merge_df=pd.merge(df1,df2,on=key)
    print("Merged dataFrame")
    print(merge_df)
    merge_df.to_csv(r"C:\Users\Zak\OneDrive\Desktop\TP OOP\new.csv",index=False)
merge_CSV(r"C:\Users\Zak\OneDrive\Desktop\ExercicesPy\‪df.csv",r"C:\Users\Zak\OneDrive\Desktop\ExercicesPy\‪merg.csv","nom")



import pandas as pd
def pandas_csv_operation(file_path):
    
    df=pd.read_csv(file_path)
    print("original Dataframe")
    print(df)
    filtered_df=df[df["age"]>18]
    print("\n filtred Datafrem (age>18): ")
    print(filtered_df)
    filtered_df.to_csv("Book.csv",index=False)
pandas_csv_operation(r"C:\Users\Zak\OneDrive\Desktop\ExercicesPy\‪df.csv")



from pandas import DataFrame
#data sous form dun disctionner
dictData={"nom":["souhaila","salma","nouha"],"age":[22,44,23],"taille":[189,120,159]}
dataFrm=DataFrame(dictData,columns=["nom","age","taille"])
export_csv=dataFrm.to_csv(r"C:\Users\Zak\OneDrive\Desktop\ExercicesPy\‪df.csv",index=None,header=False)
print(dataFrm)

