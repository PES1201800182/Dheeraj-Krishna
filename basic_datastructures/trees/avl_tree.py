class elem:
    def __init__(self,parent,value):
        self.parent=parent
        self.value=value
        self.height=0
        self.left=None
        self.right=None
def print_tree(tree):
    if(tree==None):
        return
    else:
        print('_'*tree.height,tree.value,'_'*tree.height)
        print_tree(tree.left)
        print_tree(tree.right)
def rotate(curnode,ind):
    if(ind[0]=='l'):
        final=curnode.right.height
        if ind[1]=='r':
            temp=curnode.right
            temp1=temp.left
            temp1.parent=temp.parent
            temp.parent=temp1
            temp.left=temp1.right
            temp1.right=temp
        temp=curnode.right
        temp.parent=curnode.parent
        curnode.parernt=temp
        curnode.right=temp.left
        temp.left=curnode
        if(temp.parent!=None and temp.parent.value<temp.value):
            temp.parent.right=temp
        else:
            if(temp.parent!=None):
                temp.parent.left=temp
        temp.height=final
        curnode.height=final-1
        temp.right.height=final-1
        return temp
    else:
        final=curnode.left.height
        if ind[1]=='l':
            temp=curnode.left
            temp1=curnode.right
            temp1.parent=temp.parent
            temp.parent=temp1
            temp.right=temp1.left
            temp1.left=temp
        temp=curnode.left
        temp.parent=curnode.parent
        curnode.parent=temp
        curnode.left=temp.right
        temp.right=curnode
        if(temp.parent!=None and temp.parent.value<temp.value):
            temp.parent.right=temp
        else:
            if(temp.parent!=None):
                temp.parent.left=temp
        temp.height=final
        curnode.height=final-1
        temp.right.height=final-1
        return temp
        
def insert(tree,value):
    if(tree==None):
        return elem(None,value)
    else:
        flag=1
        curnode=tree
        while(1):
            if(curnode.value==value):
                flag=0
                break
            elif curnode.value>value:
                if curnode.left!=None:
                    curnode=curnode.left
                else:
                    curnode.left=elem(curnode,value)
                    break
            else:
                if curnode.right!=None:
                    curnode=curnode.right
                else:
                    curnode.right=elem(curnode,value)
                    break
        if(flag==0):
            return tree
        while(1):
            lefth=-1
            righth=-1
            if(curnode.right!=None):
                righth=curnode.right.height
            if(curnode.left!=None):
                lefth=curnode.left.height
            if(abs(lefth-righth)>=2):
                ind=[]
                temp=0
                if(lefth>righth):
                    ind.append('r')
                    temp=curnode.left
                else:
                    ind.append('l')
                    temp=curnode.right
                if(temp.right==None):
                    ind.append('r')
                elif(temp.left==None):
                    ind.append('l')
                elif(temp.left.height>temp.right.height):
                    ind.append('r')
                else:
                    ind.append('l')
                curnode=rotate(curnode,ind)
            toth=-1
            if(curnode.left!=None):
                toth=curnode.left.height+1
            if(curnode.right!=None):
                toth=max(curnode.right.height+1,toth)
            curnode.height=toth
            if(curnode.parent==None):
                break
            curnode=curnode.parent
        
        return curnode

Tree=None
for i in range(1,7):
    Tree=insert(Tree,i)

print_tree(Tree)            
        
            
