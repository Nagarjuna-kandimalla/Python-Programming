def partition(array, low, high):
    n=  (low+high)/2
    m = (int) (n/2)
    print(f"The {low}, {high} middle pivot index is {m}, and element is {array[m]}")
    pivot = array[m]
    i = low - 1

    for j in range(low, high):
        print(f"the condition is {array[j]} <= {pivot}")
        if array[j] <= pivot:
            
            i += 1
            array[i], array[j] = array[j], array[i]
            print(f"swapped pos {i} with {j}")
        print(f"after loop {j} the array is {array}")    

    array[i+1], array[m] = array[m], array[i+1]
    print(f"after for loop the array is {array}")
    
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [1,2,3,4,5,7]
quicksort(my_array)
print("Sorted array:", my_array)
