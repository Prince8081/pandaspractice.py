import pandas as pd

#Series  (one-dimensional array store [1d data structure])

a = [1,2,3,4,5,6,7,8]
var = pd.Series(a , dtype=float)
print(var)
print(type(var))
print(var[2])

dic = {
    "Name" : ["Python" , "C" ,"C++" , "java"],
    "Por" : [12,13, 14, 15],
    "Rank" : [1, 4, 3, 2]
}

var1 = pd.Series(dic)
print(var1)
print(var1["Rank"])   #or print(var1([2]))

s = pd.Series(12 , index=[1,2,3,4,5,6,7])
print(s)

a1 = pd.Series(12 , index=[1,2,3,4,5,6,7])
a2 = pd.Series(12 , index=[1,2,3,4])
print(a1+a2)


#DataFrame   (two-dimentional array store [2d data structure])

L = [1,2,3,4,5,6]

var2 = pd.DataFrame(L)
print(var2)
print(type(var2))

d = {
    "a" : [1,2,3,4,5],
    "S" : [1,2,3,4,5],
    "d" : [1,2,3,4,5],
    "1" : [1,2,3,4,5]
}

var3 = pd.DataFrame(d)
var3 = pd.DataFrame(d , columns= (["S","1"]))     # if you want to see single column 
var3 = pd.DataFrame(d , columns= (["S","1"]) , index= ["a", "S" , "d", "f", "g"])     # if you want to change index 
print(var3)


list_1 = [[1,2,3,4,5] , [11,12,13,14,15]]

var4 = pd.DataFrame(list_1)
print(var4)
print(type(var4))

sr = {"s": pd.Series([1,2,3,4]),
      "r" : pd.Series([1,2,3,4])
}

var5 = pd.DataFrame(sr)
print(var5)
print(type(var5))


