#functions taken from stackoverflow
#ok so like, i havent touched py in a while. The comp algo has to go through 
#many iterations before it "breaks even"
def toBin(te):
    res = ''.join(format(ord(i), 'b').zfill(8) for i in te)
    return(res)
def se(item, split_num):
    return [item[i:i+split_num] for i in range(0, len(item), split_num)]


with open("file.txt","r") as file:
    text = str(file.read())
    print(text)
    string = str(toBin(text))
    print(string)
    print(len(string))
    if len(string) % 2 == 0:
        print(se(string,int(len(string)/2)))
        arr = se(string,int(len(string)/2))
    print(len(arr))
    finarr = [];
    for i in range(1,len(arr),2):
        if int(arr[i]) % 2 != 0:
            arr[i] = arr[i].replace("0","2").replace("1","4")
            print(arr)
    for i in range(0, len(arr)-1,2):   
        a = int(arr[i])+int(arr[i+1])
        if a == 1:
            a = "01"
        finarr.append(str(a))
        print(finarr)
    string = "".join(finarr)
    print("-------------------"+ str(len(string)))
    if int(len(string)) % 2 == 0:
        arr = se(string,int(len(string)/2))
    else:
        arr = se(string,1)
    newarr=[]
    for i in range(1,len(arr),2):
        if int(arr[i]) % 2 != 0:
            arr[i] = arr[i].replace("3","0").replace("4","1")
    for i in range (0,len(arr)-1,2):
        a = int(arr[i])+int(arr[i+1])
        if a >= 0 and a <10: 
            b = "0"
            c = str(a)
            a = b+c
        if a == 10:
            a == "a"
        newarr.append(str(a))
        print(newarr)
    string = "".join(newarr)
    print(len(string))
    
"""
    a = str(int(arr[0])+int(arr[1]))
    b = str(int(arr[2])+int(arr[3]))
    c = str(int(arr[4])+int(arr[5]))
    d = str(int(arr[6])+int(arr[7]))
    e = str(int(arr[8])+int(arr[9]))
    f = str(int(arr[10])+int(arr[11]))
    g = str(int(arr[12])+int(arr[13]))
    added = a+b+c+d+e+f+g
    print (added)
    print(len(str(added)))
    arr = se(str(added),1)
    arr[1] = arr[1].replace("3","0").replace("4","1")
    arr[3] = arr[3].replace("3","0").replace("4","1")
    arr[5] = arr[5].replace("3","0").replace("4","1")
    arr[7]= arr[7].replace("3","0").replace("4","1")
    arr[9] = arr[9].replace("3","0").replace("4","1")
    arr[11] = arr[11].replace("3","0").replace("4","1")
    arr[13] = arr[13].replace("3","0").replace("4","1")
    a = str(int(arr[0])+int(arr[1]))
    b = str(int(arr[2])+int(arr[3]))
    c = str(int(arr[4])+int(arr[5]))
    d = str(int(arr[6])+int(arr[7]))
    e = str(int(arr[8])+int(arr[9]))
    f = str(int(arr[10])+int(arr[11]))
    g = str(int(arr[12])+int(arr[13]))
    if len(a)>1:
        a = a.replace("10","a")
    if len(b)>1:
       b = b.replace("10","a")
    if len(c)>1:
        c = c.replace("10","a")
    if len (d)>1:
        d =d.replace("10","a")
    if len(e)>1:
        e = e.replace("10","a")
    if len(f)>1:
        f = f.replace("10","a")
    if len(g)>1:
        g = g.replace("10","a")
    added = a+b+c+d+e+f+g
    print (added)
    
    """
