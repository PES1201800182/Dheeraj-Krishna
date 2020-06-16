def nextPowerOf2(value):
    if(value==0):
        return 1
    elif(value&(value-1)==0):
        return value
    else:
        while(value&(value-1)!=0):
            value=value&(value-1)
        return value<<1
