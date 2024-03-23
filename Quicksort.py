def swap(a,b,arr):
    if a!=b:
        temp=arr[a]
        arr[a]=arr[b]
        arr[b]=temp
    
    







def partition(elements,start,end):
    pivot_index=start
    pivot=elements[pivot_index]
    
    while start<end:
         while start<len(elements) and elements[start]<=pivot:
             start+=1
         while end<len(elements) and elements[end]>pivot:
             end-=1
         if start<end:
             swap(start,end,elements)
    swap(pivot_index,end,elements)
    return end
    
def quicksort(elements,start,end):
    if start<end:
        p1=partition(elements,start,end)
        quicksort(elements,start,p1-1)
        quicksort(elements,p1+1,end)









if __name__=="__main__":
    #lis=[11,9,7,2,29,15,28]
    elements=[11,9,7,2,29,15,28]
    quicksort(elements,0,len(elements)-1)
    print(elements)
