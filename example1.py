#insertsorting
def insertsorting(array):
    if len(array)<=1:
        return array
    else:
        for j in range(1,len(array)):
            i=j-1
            tmp=array[j]
            while i>=0 and array[i]>tmp:
                array[i+1]=array[i]
                i-=1
            array[i+1]=tmp
    return array