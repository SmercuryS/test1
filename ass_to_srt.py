import re
#a = input('please enter the name of txt file\n')
with open('aa1.txt','r') as f:
    A = f.readlines()
    f.close()
Len = len(A)
for i in range(Len):
    B = re.findall(r',(.*)\d',A[i])
    C = re.findall(r',,(.*)',A[i])
    C = C[0]
    C = C[7:]
    B = B[0]
    B1 = B[0:10]
    B2 = B[11:21]
    D = '\n'+B1+' --> '+B2+'\n'
    E = '.'+'\n'
    with open('sub.txt' , 'a') as f:
        
        f.write(E)
        f.write(D)
        f.write(C)
        f.close()
#print(C)
