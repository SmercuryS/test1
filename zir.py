L=[1,2,3]
L1=[]
for i in L[0:]:
    for x in range(len(L)): 
        for j in L[i+x:]:
            L1+=L[i:j]
print(L1)