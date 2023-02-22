def binary_search(arr,start,end,search):
    mid = (start+end)//2
    if(start<=end):
        if(arr[mid] == search):
            return 1
        elif arr[mid]>search :
            return binary_search(arr,start,mid-1,search)
        else:
            return binary_search(arr,mid+1,end,search)
    else:
        return 0
    
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    result = binary_search(arr,0,len(arr)-1,5)
    if(result == 1):
        print("found")
    else:
        print("not found")