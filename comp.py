import io
#functions taken from stackoverflow
def toBin(te):
    res = ''.join(format(ord(i), 'b').zfill(8) for i in te)
    return(res)
def se(item, split_num):
    return [item[i:i+split_num] for i in range(0, len(item), split_num)]

charrarr = se("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./0123456789:;<=>?@ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ",1)
with open("file.txt",encoding="cp437") as file:
    text = str(file.read())
    print(text)
    print(len(text))
    string = str(toBin(text))
    print(string)
    print(len(string))
    if len(string) % 2 == 0:
        print(se(string,int(len(string)/2)))
        arr = se(string,int(len(string)/2))
    print(len(arr))
    finarr = [];
    for i in range(1,len(arr),2):
        if int(i) % 2 != 0:
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
    if int(len(string)) % 2 == 0:
        arr = se(string,int(len(string)/2))
    else:
        arr = se(string,1)
    finarr = []
    tarr = []
    farr = []
    for i in range(1,len(arr),2):
        if int(arr[i]) % 2 != 0:
            print(arr[i])
            farr = se(arr[i],1)
            print(farr)
            for j in range(0, len(farr),1):
                farr[j] = farr[j].replace("a","x").replace("9","y").replace("8","99").replace("7","88").replace("6","77").replace("5","66").replace("4","55").replace("3","44").replace("2","33").replace("1","22").replace("0","11")
                farr[j] = farr[j].replace("x","121").replace("y","110")
            print(arr[i])
            arr[i] = "".join(farr)
            print("idhuigfdygafjsgfasgfhkhfjhghagfkashgkafjgsk")
            print(arr[i])
            tarr = se(arr[i],2)
            print(tarr)
    for i in range(0,len(arr)-1,2):
        if len(arr) == 2:
            ca = arr[0]
            ca = se(ca,1)
            cb = "".join(tarr)
            cb = se(cb,2)
            print(ca)
            print("ca")
            print("cb")
            print(cb)
        for i in range(0,len(ca),1):
            
            a = int(ca[i]) + int(cb[i])
            if int(a) >=0 and int(a) < 10:
                b = "0"
                c = str(a)
                a = b+c
            if int(a) > 10:
                print(a)
                print 
                a = charrarr[int(a)]
            finarr.append(str(a))
            print(finarr)
            print(len(finarr))
        
       
    with open("compressed.txt","w",encoding="utf-8") as tf:
        tf.write("".join(finarr))
        #You may notice, that the final file size is either larger, or exactly the same as input file. We will need to compress it one more time. But this requires math that i dont feel like doing yet 
        #Feel free to try your hand at the next iteration!
        
