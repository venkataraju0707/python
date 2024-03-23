def Bubblesort(list):
    size=len(list)
    for i in range(size-1):
        swapped=False
        for j in range(size-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                swapped=True
        if swapped ==False:
            break
    return list 
            








if __name__=="__main__":
    #list=[86,65,99,23,14,5,2]
    list=[1,2,3,4,5,6]
    print(Bubblesort(list))
