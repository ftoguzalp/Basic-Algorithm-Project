
import pandas as pd
import numpy as np




z = "True"
while True:
    if z =="True":
        x=int(input("Değer girin:"))
        z=input("Devam etmek istiyorsanız True Yazın.")
    elif z != "True":
        break

y=[]


n=2**(x-1)
for m in range(n) :
   y=np.ones(n)


print((y))