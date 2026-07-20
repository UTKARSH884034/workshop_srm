def sortlist(l):
    for y in range (0,len(l)):
        for j in range (0,len(l)-y-1):
            if l[j]>l[j+1]:
                l[j+1],l[j]=l[j],l[j+1]
    return (l)
if __name__ == '__main__':
    l=[1,2,3,5,4,6,7,9,3,1,2]
    print(sortlist(l))