
arr = [2,4,6,3,7,9,3,4,6,8,7,1]

def swap(left, right):
    tmp = arr[left]
    arr[left] = arr[right]
    arr[right] = tmp

def sort(left, right):
    print "before sort left:%4d, right:%4d arr:%s"%(left, right, arr)
    if left >= right:
        return
    beginleft = left
    beginright = right

    index = right
    right = right - 1 
    while left < right:
        while (arr[left] < arr[index]) and (left < right):
            left = left+1

        while (arr[right] > arr[index]) and (left < right):
            right = right-1

        if left < right:
            swap(left, right)
    if arr[left] >= arr[index]:
        swap(left, index)
        index = left
    print "after  sort left:%4d, right:%4d arr:%s"%(left, right, arr)

    sort(beginleft, index-1)
    sort(index+1, beginright)

if __name__ == "__main__":
    sort(0, len(arr)-1)
    print arr
