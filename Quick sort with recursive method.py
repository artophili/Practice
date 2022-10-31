#QUICK SORT RECURSION
def partition(a):   #should return a index of pivot element
    ele = a[0]
    count = 0   #To count the number of elements less than the first element
    for i in range(len(a)):
        if a[i] < ele:
            count += 1
    a[0],a[count] = a[count],a[0]
    
    return count
    


def QuickSort(a):
    l = len(a)
    if l == 0 and l == 1:
        return a
    
    i = partition(a)#function to partition given array
    QuickSort(a)
    QuickSort(a)
    return a
a = [3,4,5,1,2,6,7,8]
re = QuickSort(a)
print(re)
