def chmchm(l,a):
    last=len(l)-1
    first=0
    res_list=[]
    while first<last:
        if l[last]+l[first]>a:
            last-=1
        elif l[last]+l[first]<a:
            first+=1
        else:
            res_list.append((first,last))
            first+=1
            last-=1
    return res_list
print(chmchm([1,2,3,4,5,6],7))