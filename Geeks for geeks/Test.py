

def partition(array, low, high):
  pivot = array[high]

  for i in range(low, high):
     if array[i]<pivot:
        print("pivot is greater")
     else:
        print(f"coming into else block for elements {array[i], array[high]}")
        array[i], array[high]  = array[high], array[i]
        print(array)
  return i+1        



def Qsort(array, low=0, high=None):
    if high==None:
        high = len(array)-1

    p_i= partition(array, low, high)
    print(f"{p_i}")
    Qsort(array, low, p_i-1)
    Qsort(array, p_i+1, high)    
    return array       

arr = [5,10,4,2,11]
Qsort(arr)



