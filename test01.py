import hashlib
#import pickle

user = input('Enter your Username \n')


with open('User_list.txt' , 'r') as f:
    a = f.readlines()
    c = 0
    A = []
    for i in a :
        x = a[c]
        x = x[:-1]
        A.append(x)
        c += 1
    f.close()

if user in A :
    print('this username already taken')
    

else:
    with open('User_list.txt' , 'a+') as f:
        f.write(user)
        f.write('\n')
        f.close()

    a = bytes(user,'utf-8')

    m = hashlib.sha256()
    m.update(a)
    a = m.hexdigest()
    #print(a)

def sort_user():
    with open('User_list.txt' , 'w') as f:
        a = f.readlines()    
