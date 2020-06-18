def intialize_fenwik(actual_tree,fenwik_tree):
    length=len(actual_tree)
    for i in range(length):
        k=i+1
        while True:
            if k>length:
                break
            fenwik_tree[k]+=actual_tree[i]
            k=k+(k&(-k))
def give_sum(fenwik_tree,index):
    summ=0
    while(index>0):
        summ+=fenwik_tree[index]
        index-=(index&(-index))
    return summ
def find_sum(fenwik_tree,start,end):
    if(start==end):
        return fenwik_tree[start]
    elif(start>end):
        temp=start
        start=end
        end=temp
    res1=give_sum(fenwik_tree,start+1)
    res2=give_sum(fenwik_tree,end+1)
    return res2-res1+fenwik_tree[start+1]
