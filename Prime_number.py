import json
prime_db = []
try:
    with open('prime.json', 'r') as fp:
        prime_db = json.load(fp)
except:
    with open('prime.json', 'w') as fp:
        json.dump(prime_db,fp)
def isPrime(x):
    if(x==0 or x==1):
        return False
    for i in prime_db:
        if(x%i==0):
            return False
    return True

def findPrime(start,end):
    x = prime_db[len(prime_db)-1]
    start_index = start
    end_index = end
    # for i in range(start-50,start+50):
    #     x_index = prime_db.index(i)
    #     if(prime_db[x_index]<=start):
    #         start_index = x_index
    # for i in range(end-50,end+50):
    #     x_index = prime_db.index(i)
    #     if(prime_db[x_index]<=end):
    #         end_index = x_index
    while x<=end:
        # print(x)
        if(isPrime(x)):
            print(x)
            prime_db.append(x)
            with open('prime.json','w') as fp:
                json.dump(prime_db,fp)
        if(x>=3):
            x+=2
        else:
            x+=1
    # ret = []
    # while start <= prime_db[i] <= end:
    #     print prime_db[i]
print(pow(2,20)-1)
findPrime(pow(2,20)-1,pow(2,25)-1)
selisih = []
for i in range(1,len(prime_db)):
    selisih.append(prime_db[i]-prime_db[i-1])
# print(prime_db)
index = selisih.index(max(selisih))
print(index,prime_db[index-1],prime_db[index]-prime_db[index-1],prime_db[index],prime_db[index+1]-prime_db[index],prime_db[index+1])