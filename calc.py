from itertools import permutations
from itertools import product

op=["+","-","*","/"]
numbers = [3, 4, 5, 6]
kakko=["(",")"]

check=[0]*10000

for combination in permutations(range(4), r=4):
    for operate in product(op, repeat=3):
        
        for j in range(7):
            if j ==0:
                #A $ B $ C $ D
                sol = str(numbers[combination[0]]) + operate[0] +str(numbers[combination[1]])+ operate[1] +str(numbers[combination[2]])+ operate[2] +str(numbers[combination[3]])
            elif j ==1:
                #{A $ B} $ C $ D
                sol = str(kakko[0])+str(numbers[combination[0]]) + operate[0]+str(numbers[combination[1]])+str(kakko[1])+ operate[1] +str(numbers[combination[2]])+ operate[2] +str(numbers[combination[3]])
            elif j ==2:
                #A $ B $ {C $ D}
                sol = str(numbers[combination[0]]) + operate[0] +str(numbers[combination[1]])+ operate[1] +str(numbers[combination[2]])+ operate[2] +str(numbers[combination[3]])
            elif j ==3:
                #A $ {B $ C} $ D
                sol = str(numbers[combination[0]]) + operate[0] +str(numbers[combination[1]])+ operate[1] +str(kakko[0])+str(numbers[combination[2]])+ operate[2] +str(numbers[combination[3]])+str(kakko[1])
            elif j ==4:
                #{A $ B} $ {C $ D}
                sol = str(kakko[0])+str(numbers[combination[0]]) + operate[0] +str(numbers[combination[1]])+str(kakko[1])+ operate[1] +str(kakko[0])+str(numbers[combination[2]])+ operate[2] +str(numbers[combination[3]])+str(kakko[1])
            elif j ==5:
                #{A $ B $ C} $ D
                sol = str(kakko[0])+str(numbers[combination[0]]) + operate[0] +str(numbers[combination[1]])+ operate[1] +str(numbers[combination[2]])+str(kakko[1])+ operate[2] +str(numbers[combination[3]])
            elif j ==6:
                #A $ {B $ C $ D}
                sol = str(numbers[combination[0]]) + operate[0] +kakko[0]+str(numbers[combination[1]])+ operate[1] +str(numbers[combination[2]])+ operate[2] +str(numbers[combination[3]])+kakko[1]

            result = eval(sol) 
            if(result==41): #解答の手法を示す。
                print(sol)
            check_int =int(result)

            if result>=0:
                #print(f"{sol}={result}")
                if isinstance(result, int)or result.is_integer():
                    check[check_int] = check_int
                    #print(f"{sol}={result}")


flag=0

for i in range(1,100):
    if check[i]==0:
        if flag ==0:
            print(f"最小の数字は{i}となっています。")
            flag +=1
            continue
    if check[i]==0:
        if flag ==1:
            print(f"次に小さい値は{i}となっています。")
            flag +=1
