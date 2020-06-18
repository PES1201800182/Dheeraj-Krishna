from math import *
def nextPowerOf2(value):
    if(value==0):
        return 1
    elif(value&(value-1)==0):
        return value
    else:
        while(value&(value-1)!=0):
            value=value&(value-1)
        return value<<1
class segment_node:
    def __init__(self,start,end,value):
        self.start=start
        self.end=end
        self.value=value
def segment(array,segment_tree,start,end,index):
    segment_tree[index].start=start
    segment_tree[index].end=end
    if(start==end):
        segment_tree[index].value=array[start]
        return
    else:
        mid=floor((end+start)/2)
        if(mid>=start):
            segment(array,segment_tree,start,mid,2*index+1)
        if(mid<end):
            segment(array,segment_tree,mid+1,end,2*index+2)
        segment_tree[index].value=min(segment_tree[2*index+1].value,segment_tree[2*index+2].value)
def givemin(segment_tree,start,end,ind):
    if(start<=segment_tree[ind].start and end>=segment_tree[ind].end):
        return segment_tree[ind].value
    elif((end<segment_tree[ind].end and end<segment_tree[ind].start) or (start>segment_tree[ind].start and start>segment_tree[ind].end)):
        return inf
    else:
        return min(givemin(segment_tree,start,end,2*ind+1),givemin(segment_tree,start,end,2*ind+2))
def change_index(segment_tree,index,value):
    segment_tree[index].value=value
    child=index
    parent=floor((child-1)/2)
    while(child>0 and segment_tree[child].value<segment_tree[parent].value):
        segment_tree[parent].value=segment_tree[child].value
        temp=child
        child=parent
        parent=floor((child-1)/2)
        
array=input().split()
for i in range(len(array)):
    array[i]=int(array[i])
segment_tree=[]
for i in range(2*nextPowerOf2(len(array))-1):
    segment_tree.append(segment_node(-inf,inf,inf))
segment(array,segment_tree,0,len(array)-1,0)
print(givemin(segment_tree,3,6,0))
change_index(segment_tree,4,-100)
print(givemin(segment_tree,0,6,0))

