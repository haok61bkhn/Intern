import re
from sklearn.metrics import accuracy_score
data=[] # moi phan tu la từ và số lượng từ
lam=[] # mỗi phần tử là từ trong data và lamda của nó trong 1 label
sizelam=0; 
    
def readFile(path): # doc file tra ve xau
    f=open(path,"r",encoding="utf-8")
    s=f.read().split("\n")
    s.pop()
    return (s)         

def prepare(s): # tien xu li mang xau
    for i in range(0,len(s)):
        s[i] = re.sub("%|:|'|@|#|\$|\,|\"|\(|\)|&|\*|Nguồn.*|[0-9]|\/|\.|\“|’|;| - |\]|\[|\?" , '',s[i])
        s[i] = re.sub("[\t]|  |   | - ", " ",s[i])
    
def Prepare_Data():    # tien xu li data 
    for i in range(1,14):
        data.append([])
        s=readFile("classify_data/train/"+str(i)+ ".txt")
        prepare(s)
        for j in range(0,len(s)):
            data[i-1]+=s[j].split(" ")



def Cal_lamda():    #  tao vecto va tinh lamda
   dx={}
   for i in range(0,13):
       dx.update(dict.fromkeys(data[i],0))
   sizelam=len(dx)
   for i in range(0,13):
        lam.append([])
        lam[i]=dx.copy()
        for x in data[i]:
            lam[i][x]+=1
  
   for i in range(0,13):
        sizedata=len(data[i])
        sums=sizedata+sizelam
        for x in lam[i]:
            lam[i][x]=(lam[i][x]+1)/sums
             

    
def Check(s): # tien xu li xau s va du doan label s
    import math
    s=s.split(" ")
    lams={}
    lams=dict.fromkeys(s,0)
    for x in s:
        lams[x]+=1
    res=-100000
    label=0
   
    for i in range(0,13):
        su=0.0
        count=0
        for x in lams:
            if (x in lam[i]) and (len(x)>=3): 
                su+=lams[x]*math.log10(2*lam[i][x])        
        if res<su : 
            res=su
            label=i+1
    
    return label

    
        

if __name__ == "__main__":
       
    Prepare_Data()
    Cal_lamda()

    s=readFile("classify_data/test/data.txt")
    prepare(s)
    f=open("res.txt","w+",encoding="utf-8")
    res=[] # mảng dự đooán label của test
    
    for x in s:
        z=Check(x)
        f.writelines(str(z)+"\n")
        res.append(str(z))
    
    res_main=readFile("classify_data/test/label.txt") # mảng kết của đúng của test
    print(accuracy_score(res_main,res))
    
    
    
   

    

    
       

     
       
        