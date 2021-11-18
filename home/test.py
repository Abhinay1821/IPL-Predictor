import pickle

with open('model_pickle','rb') as f:
    mp= pickle.load(f)

ans=0
def fun(inn,overi,balli,overf,ballf):
    global ans

    ans=0
    for i in range(balli,7):
        ans+= (mp.predict([[inn,overi,i]])[0])
    
    for i in range(overi+1,overf):
        for j in range(1,6):
          ans+= (mp.predict([[inn,i,j]])[0])
    for i in range(1,ballf+1):
        ans+= (mp.predict([[inn,overf,i]])[0])

    return ans   