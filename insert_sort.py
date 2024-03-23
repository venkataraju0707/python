def insert_sort(elements):
    for i in range(1,len(elements)):
        anchor=elements[i]
        j=i-1
        while j>=0 and anchor<elements[j]:
            elements[j+1]=elements[j]
            j=j-1
        elements[j+1]=anchor
        
                   










if __name__=="__main__":
    elements=[5,10,3,15,70,1]
    insert_sort(elements)
    print(elements)
