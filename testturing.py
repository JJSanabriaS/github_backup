strs=['10.98.162.168','2001:0db8:85a3:0000:0000:8a2e:0370:7334','255.32.555.5','250.32:555.5','192.168.100.23','92.0.2.146', '192.168.1.1', '172.16.254.1', '1.2.3.4','01.102.103.104']
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("cadena input")

for string in range(0,len(strs)):
    print(strs[string])
   # print(len((strs[string])))
    if len(strs[string])>15:
        indexes = [x for x, v in enumerate(strs[string]) if v==':']
        indexes.insert(0,0)
        indexes.append(len(strs[string]))
        #print(indexes) # <-- [6, 13, 19]
        if len(indexes)== 9:
            bool6= 1
    else:
    #    print("cadena")
       # print(len(strings))
        indexes = [x for x, v in enumerate(strs[string]) if v=='.']
      #  print(indexes) # <-- [6, 13, 19]
  #      print(type(indexes))
        indexes.insert(0,0)
        indexes.append(len(strs[string]))
       # print(len(indexes))
       # print(indexes)
        count=0
        if len(indexes)==5:
            for ind in range(0,4,1):
                #print("ind",ind)
                #print(indexes[ind])
                subs=strs[string][indexes[ind]:indexes[ind+1]]
                #print("subs",subs)
                indexes2 = [x for x, v in enumerate(subs) if v=='.']
                #subsnumeric = re.sub(r'\D', '', subs)
                #print(indexes2)
                #print(type(indexes2))
                #print(len(indexes2))
                if len(indexes2)>0:
                    subsnumeric=subs[1:]
                else:
                    subsnumeric=subs[0:]
                
               # print(subsnumeric)
                if (0<int(subsnumeric)<255):
                    count=count+1
#
           # print(count)
            if count<3:
                bool6=3
            else:
                bool6=2







    print("valor bool")
    print(bool6)
    if (bool6==1): print("ipv6")
    elif (bool6==2): print ("ipv4")
    else: print("none")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
