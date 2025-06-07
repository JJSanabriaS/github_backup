wood=[23, 23, 2, 21, 5, 19, 23, 17, 6, 22, 6]

print(wood)
secwood=wood.sort()
#print(wood)
#print(len(wood))
#print((set(wood)))
#print(len(set(wood)))
uniqes=list(set(wood))
sumaq=0
#print((set(wood))) ^ ((set(wood)))
my_dict = {}
for j in range(0,len(set(wood))):
    count=0        
    for x in range(0,len(wood)):
        #print("elementos en comparacion")
 #       print("elementos   ", uniqes[j],"      ",wood[x])
        #print("elemento original",wood[x])
        #print(count)
        if int(uniqes[j])==int(wood[x]):
            count=count+1
  #          print("acontencio ocurrencia   ",count)
            if count > 1:
                sumaq=sumaq+1
   #             print("contador ocurrencias extras")
   #             print(sumaq)
        
    #    print("elemento unico",uniqes[j],"  contador ", count," ocurrencias  ", sumaq)
        my_dict[str(uniqes[j])] = count
        
print(my_dict)

#print(max(wood))
#print(len(wood)-1)
indexes = [x for x, v in enumerate(wood) if v==max(my_dict, key=my_dict.get)]
#print(len(indexes))
#print(indexes)
indexes1=[x for x in range(0,len(wood))]
#print(indexes1)

res = list(set(indexes1) - set(indexes))
#print(len(res))
#print("++")
#print(res)
cont1=0
for i in range (0,len(res)):
    for j in range (i,len(res)):
        if int(wood[res[j]])!=0 or int(wood[res[i]])!=0:
            nuew=int(wood[res[i]])+int(wood[res[j]])
            if (nuew==int(max(my_dict, key=my_dict.get))):
                print(i,j,(wood[res[i]]),int(wood[res[j]]),nuew)
                print(nuew)
                cont1=cont1+1

print("most frequent ",max(my_dict, key=my_dict.get), "freq ocurrencias ",my_dict.get(max(my_dict, key=my_dict.get)))
print(cont1)
#print(len(indexes))
print("madeiras obtidas  ", my_dict.get(max(my_dict, key=my_dict.get))+cont1)
