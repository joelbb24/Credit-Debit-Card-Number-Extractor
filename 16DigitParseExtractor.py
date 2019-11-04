
def parseTree(s):
    count = 0
    n = len(s)
    list1 = []
    list2 = []
    for i in range(n):
        if s[i].isdigit():
            count += 1
            list1.append(s[i])
            if count == 16 and i+1<n:
                if s[i+1].isdigit():
                    newS = s.split()
                    for a in range(0,len(newS)-1):
                        if len(newS[a]) + len(newS[a+1]) == 16:
                            newStr = newS[a]+" "+newS[a+1]
                            list2.append(newStr)
                        else:
                            continue
            elif count == 16 and i+1>n:
                list2.append("".join(list1).strip())
                
            
        elif s[i]==" ":
            list1.append(s[i])
        else:
            count = 0
            list1 = []        

        while count==16 and i<n:
            if i+1<n and s[i]==" ":
                list2.append("".join(list1).strip())
                list1 = []
                count = 0
            elif i+1<n and s[i+1]==" ":
                list2.append("".join(list1).strip())
                list1 = []
                count = 0
            elif i+1<n and s[i+1].isalpha():
                list2.append("".join(list1).strip())
                list1 = []
                count = 0
            elif i+1<n and s[i+1].isdigit():
                count = 0
                list1 = []
                break
            elif i+1==n and s[i]!=" ":
                list2.append("".join(list1).strip())
            else:
                count = 0
            i = i + 1
