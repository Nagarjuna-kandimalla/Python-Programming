l = [10, 40,50,60,20, 10,10, 40,30, 30, 20]
#count distinct element and the number of it
#skip_Index = []
de = []

"""for x in range(len(l)):
    if(x not in skip_Index):
     for y in range((x+1),len(l)):
       
         if (l[x]==l[y]):
            skip_Index.append(y)
            print(f"skip index child is {skip_Index}")
         else:
            print(f"{l[y]} doesn't match with {l[x]}")
    else:
        print(f"the iteration is skipped for {x}")    

for x in range(len(l)):
    if x not in skip_Index:
     print(f"distinct elements are {l[x]}")    """

for x in l:
    if x not in de:
       de.append(x)
print(f"distinct elemts are {de} and count is {len(de)}")  
des=["Rahul","vikas"]
print(des[1][-2])     

    

