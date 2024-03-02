import math
def inRange(a,b,c,fn,n):
    fnx = a*n + b*n*math.floor(math.log(n,2)) + c*pow(n,3)
    if(fnx<=fn):
        return True
    else:
        return False

def find_digit(a,b,c,fn,n=1):
    while inRange(a,b,c,fn,n):
        n = n * 10
    n = math.floor(n/10)
    n = math.floor(math.log(n,10)) + 1
    return n
        
def fxn(a,b,c,fn):
    n = 0
    n_digit = find_digit(a,b,c,fn)
    # print("n_digit",n_digit)

    #find Number as long as digit from Most Significant Number to Least Significant Number
    for i in range(1,n_digit+1):
        x_val = 0
        for j in range(1,99):
            x_val = math.floor(j*pow(10,n_digit-i))
            # print(x_val)
            if(not inRange(a,b,c,fn,n+x_val)):
                x_val = math.floor((j-1)*pow(10,n_digit-i))
                break
        n = n + x_val
        # print(i,n)
    return n

def generate_test_case(a,b,c,n):
    fn = a*n + b*n*math.floor(math.log(n,2)) + c*pow(n,3)
    return str(a)+" "+str(b)+" "+str(c)+" "+str(fn)

gen_case = [
    [1,1,0,1],
    [2,1,0,11],
    [12,21,0,123],
    [12,21,0,12345],
    [12,15,0,1234567],
    [12,15,0,12345678],
    [76,98,0,123456789],
    [81,96,0,1234567890],
    [13,5,1,12345678901],
    [17,4,2,123456789012],
    [17,4,2,1234567890123],
    [17,4,2,92345678901234],
    [17,4,2,923456789012345],
    [17,4,2,923456789012383624832684362846382645127352137217352458214456],
    [1,1,0,pow(2,1026)-1]
]

print("Input :")
test_case = []
for i in range(len(gen_case)):
    a,b,c,n = gen_case[i]
    test_case.append(generate_test_case(a,b,c,n))
    print(test_case[i])

# print("\nExpected Result :")
# for i in range(len(expected_result)):
#     print(expected_result[i])

expected_result = []
print("\nExpected Result")
for i in range(len(gen_case)):
    a,b,c,n = gen_case[i]
    expected_result.append("#%d"%(i+1)+" %d"%n)
    print("#%d"%(i+1)+" %d"%n)

import time
start = time.time()
print("\nOutput :")
for i in range(1,len(test_case)+1):
    a,b,c,fn = map(int, test_case[i-1].split())
    result = fxn(a,b,c,fn)
    isOk = "Wrong"
    if(str("#%d"%i+" %d"%result)==expected_result[i-1]):
        isOk = "OK"
    print("#%d"%i," %d"%result," ",isOk)
end = time.time()
print("\nStart\t\t:",start)
print("End\t\t:",end)
print("Execution Time\t:",(end-start)*1000000," us\n")

# import json
# prime_db = []
# with open('./python/prime.json', 'r') as fp:
#     prime_db = json.load(fp)

# print(len(prime_db))
print((pow(2,22)-1),(pow(2,22)-1)-(pow(2,20)-1),(pow(2,20)-1))


print(pow(2,14284)-1)
# for n in range(1,100):
#     if(not (pow(2,n)-1)%3 == 0 and not (pow(2,n)-1)%5 == 0 and not (pow(2,n)-1)%7 == 0):
#         print(n,pow(2,n)-1)