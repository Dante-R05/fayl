import os
os.system("cls")

def func(n):
    son=2
    while son<=n:
        count=0
        i=1
        while i<=son:
            if son%i==0:
                count+=1
            i+=1
        if count==2:
            print(son)
        son+=1            
n=20

func(n)