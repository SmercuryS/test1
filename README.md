A =[ int(x) for x in input().split(',') ]

for i in range(n*m+1,0,-1):
    if n%i==0 and m%i==0 :
        print(i)
        break
