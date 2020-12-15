#Used code from Geeksforgeeks
import numpy as np

def hasArrayTwoCandidates(A, arr_size, sum):
     
    # sort the array
    quickSort(A, 0, arr_size-1)
    l = 0
    p = 1
    r = arr_size-1
     
    # traverse the array for the two elements, and return the product if the sum is correct
    while p<r:
        if (A[l] + A[r] == sum):
            return A[l]*A[r]
        elif (A[l] + A[r] < sum):
            p += 1
        else:
            r -= 1
 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
     
 
# Driver program to test the functions
if __name__ == "__main__":
    with open('input.txt') as f:
        numbers = f.readlines()
        A = [int(x.strip()) for x in numbers]
    n = 2020
    print(hasArrayTwoCandidates(A, len(A), n))
