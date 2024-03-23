def linear_search(list_of_numbers,num):
    for index,ele in enumerate(list_of_numbers):
        if ele ==num:
            return index
def binary_search(list_of_numbers,num):
    right_pointer=len(list_of_numbers)-1
    left_pointer=0
    mid_value=0
    while left_pointer<=right_pointer:
        mid_value=left_pointer+right_pointer//2
        if list_of_numbers[mid_value]==num:
            return mid_value
        if list_of_numbers[mid_value]<num:
            left_pointer=mid_value+1
        else:
            right_pointer=mid_value-1
    return -1        

            
            
if __name__=="__main__":
    lis=[5,3,67,89,2,4,6,10]
    print(linear_search(lis,89))
    print(binary_search(lis,89))


