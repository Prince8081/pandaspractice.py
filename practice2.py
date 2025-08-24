import pandas as pd 

#Arithmetic operations

var = pd.DataFrame({
    "A" : [1,2,3,4],
    "B" : [5,6,7,8]
})

var["C"] = var["A"]+var["B"]
var["D"] = var["A"]-var["B"]
var["E"] = var["A"]*var["B"]
var["F"] = var["A"]/var["B"]
print(var)

var1 = pd.DataFrame({
    "A" : [10,20,30,40],
    "B" : [15,16,17,18]
})
var1["P"] = var1["A"] <= 20
var1["R"] = var1['B'] >= 16
print(var1)


#Delete & Insert function 

#Insert 

var2 = pd.DataFrame({
         "A" : [1,2,3,4,5],
         "B" : [9,8,7,6,5]      
})
var2.insert(1 , "Python" , var2["A"])
var2.insert(2 , "Python1" , [11,12,13,14,15])

var2["Python_12"] = var2["A"][:3]
print(var2)


#Delete 

var2.pop("Python")     #pop , del
del var2["Python_12"]
print(var2)


#Write (create) CSV Files

dis = {
    "a" : [1,2,3,4,5,6],
    "d" : [1,2,3,4,5,6]
}
d = pd.DataFrame(dis)
print(d)

d.to_csv("Pyt.csv", index=False)   # index=False mean index not 
d.to_csv("Pyt_1.csv", index=False , header=["A","B"])                # header create own head n data


#Read CSV Files 

csv_1 = pd.read_csv('Employee.csv')
csv_2 = pd.read_csv('Employee.csv' , nrows=3)                         #nrowa give first n rows in data
csv_3 = pd.read_csv('Employee.csv' , usecols=["Gender" , "City"])     #usecols give a hole column 
csv_4 = pd.read_csv('Employee.csv' , usecols=[0,3])                   # we can use index
csv_5 = pd.read_csv('Employee.csv' , skiprows=[3 ,4])                 #skiprows  skip a row
csv_6 = pd.read_csv('Employee.csv' , index_col="Education")           # index_col create column to index        
csv_7 = pd.read_csv('Employee.csv' , header=1)                        # header convert selected row to head      
csv_8 = pd.read_csv('Employee.csv' ,names= ["col1","col2"])           # names column name change
csv_9 = pd.read_csv('Employee.csv' ,header=None )          
print(csv_9)


# Pandas function

csv1 = pd.read_csv("Employee.csv")
print(csv1)

print(csv1.describe())
print(csv1.head())
print(csv1.tail())
print(csv1[:5])                 #give first 5 rows 

print(csv1.to_numpy())         # convert into numpy array

import numpy as np 
print(np.array(csv1))            # convert into numpy array

print(csv1.sort_index(axis=0 , ascending=False))      #sort the data 0 mean row wise 

print(csv1.loc[[2,3], ["Education"]])            # 2,3row data of education sow 
print(csv1.loc[[2,3] [:]])                        # 2,3row data of all column  sow 
print(csv1.iloc[:2])                   # 2  give 

#dropna & fillna

var_2 = pd.read_csv("Employee.csv")
print(var_2.dropna())                         # dropna drop the blanks in data  row ke along drop hua hai
print(var_2.dropna(axis=1))                    # dropna drop the blanks in data  column ke along drop hua hai
print(var_2.dropna(subset=["Age"]))              # dropna drop the blanks in data named column ke along drop hua hai

#fillna

print(var_2.fillna("P"))                        #blanks fill by p


