class ar_class :
    def __init__(self,value,value1,length):
        self.value=value
        self.value1=value1
        self.array=[0]*(length+1)
def knapsack01_matrix(totwt,array,array1):
    matrix=[]
    for i in range(len(array)):
        matrix.append(ar_class(array[i],array1[i],totwt))
    for i in range(len(matrix)):
        for j in range(len(matrix[i].array)):
            if(j<matrix[i].value):
                if(i>0):
                    matrix[i].array[j]=matrix[i-1].array[j]
                continue
            else:
                temp=0
                temp1=0
                if(i>0):
                    temp=matrix[i-1].array[j-matrix[i].value]
                    temp1=matrix[i-1].array[j]
                matrix[i].array[j]=max(matrix[i].value1+temp,temp1)
    return matrix
def knapsack01_max(totwt,array,array1):
    matrix=knapsack01_matrix(totwt,array,array1)
    return matrix[len(matrix)-1].array[totwt]
def knapsack01_list(totwt,array,array1):
    matrix=knapsack01_matrix(totwt,array,array1)
    curj=totwt
    curi=len(matrix)-1
    res=[]
    while(curi>=0):
        if(curi==0):
            res.append(matrix[curi].value)
            break
        if(matrix[curi].array[curj]==matrix[curi-1].array[curj]):
            curi-=1
            continue
        res.append(matrix[curi].value)
        curj=curj-matrix[curi].value
        if(curj<=0):
            break
    return res
        
    
totwt=7
array=[5,4,3,1]
array1=[7,5,4,1]
res=knapsack01_list(totwt,array,array1)
print(res)
