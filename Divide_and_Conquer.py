import statistics
import random
import time


'''
These Algorithms all find kth smallest value in the an unsorted list. Meaning 
that if the list where sorted it would find kth value. Because the list is 
unsorted, the code cannot just index at the kth value the code must use a 
algorithm to find the kth smallest value. This project shows the use of 
different divide and conquer algorithms to solve this issue and then compares
the efficiency
'''

#############################################################################

'''
Algorithm 1:

Algorithm 1 is like an algorithm that takes a random integer in the list and 
sets it as the median. Then it creates 3 different lists a arrR, arrM and arrL.
-All values less than the median are stored into the arrL
-All values greater than the median are stored into the arrR 
-All values equal to the median are stored in arrM
then it compares the lengths of the arrays with the kth value
- if the length arrL is great than k 
    - then run algo1 on arrL with (k) 
-if length of arrL and arrM is less than k 
    - then run algo1 on arrR with (k- the sum of the lengths of arrL and arrM)
-otherwise return the median value

This splits the array into 3 different arrays and then uses comparisons to see 
what the kth value is this is a common use of the divide and conquer technique
'''
def algo1(arr,k):
    median= int 
    if (len(arr)<k):
        return -1
    
    median =arr[random.randint(0,len(arr)-1)]
    arrL=list()
    arrR=list()
    arrM=list()
    for i in range (len(arr)):
        if arr[i]<median:
            arrL.append(arr[i])
        elif arr[i] == median:
            arrM.append(arr[i])
        else:
            arrR.append(arr[i])
    if len(arrL)>=k:
        return algo1(arrL,k)
    elif (len(arrL)+len(arrM))<k:
        return algo1(arrR,(k-(len(arrL)+len(arrM))))
    else:
        return median               

'''
Algorithm 2: 

Algorithm 2 is very similar to algorithm 1 except that is first finds the 
median of the list by finding taking certain defining numbers and running them
through the algorithm. After finding the median it will assign this value to M
then it will use the same process as in one to find the kth smallest value. 
'''

              
def algo2(arr,k):
    if len(arr)<=10:
        arr.sort()
        return arr[k-1]
    
    S=list()
    x=list()
    
    for i in range(0,(len(arr)//5)):
        for j in range((i*5),(4+i*5)):
            S.append(arr[j])
        S.sort()
        x.append(algo2(S,3))
        S.clear()

        
    M=algo2(x,len(arr)//10)
    L1=list()
    L2=list()
    L3=list()
    for i in range (len(arr)):
        if arr[i]<M:
            L1.append(arr[i])
        elif arr[i] == M:
            L2.append(arr[i])
        else:
            L3.append(arr[i])
    
    if k <= len(L1):
        return algo2(L1,k)
    elif (k > len(L1)+len(L2)):
        return algo2(L3,k-len(L1)-len(L2))
    else:
        return M


'''
This is a helper function used in algorithm 3
'''

def partition(arr, lo, hi):
    swap=int
    pivot=int
    i=int
    pivot = arr[hi]
    i = lo
    for j in range(lo,hi):
        if arr[j] < pivot:
            swap= arr[i] 
            arr[i]=arr[j]
            arr[j]=swap
            i = i + 1
    swap =arr[i] 
    arr[i]=arr[hi]
    arr[hi]=swap
    return i
'''
Algorithm 3:

Algorithm 3 takes in a high and a low value and will sort the array. This 
algroithm uses the partitioning function which is like a quick sort that 
switchs numbers until they are in order. this does this by setting a pivot and
swapping the numbers around this pivot. The algorithm3 runs this on the upper 
half and lower half of array. Partion will return a value i that is the index. 

'''

def algo3(arr, lo, hi):
    p=int
    if lo < hi:
        p = partition(arr, lo, hi)
        algo3(arr, lo, p - 1)
        algo3(arr, p + 1, hi)
        
'''
this function just runs Algorithm 3 until the orginal array is completely sorted
then it will just return the kth value. 
'''
        
def sort_find(arr,k):
    algo3(arr, 0, (len(arr)-1))
    return arr[k]
    
###############################################################################
    
# A list where when k=10 the value is 7, just a controled simple test case
list1=[7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15] 
#assigning k to a value
k=10
#prints the kth smallest value
print("Result algo1:",algo1(list1,10))
print("Result algo2:",algo2(list1,10))
print("Result algo3:",sort_find(list1,k))

list2=list()
#creates a list with 10^7 integers spanning from 0-10^5 
for i in range(10**7):
    list2.append(random.randint(0,10**5))
#prints the results and the time it takes to get the results 
timestart=time.time();
print("Result algo1:",algo1(list2,5000000))
timeend=time.time();
print("Time algo1:",timeend-timestart);
timestart=time.time();
print("Result algo2:",algo2(list2,5000000))
timeend=time.time();
print("Time algo2:",timeend-timestart);
timestart=time.time();
print("Result algo3:",sort_find(list2,5000000))
timeend=time.time();
print("Time algo3:",timeend-timestart);


#############################################################################

'''
Overall we can see algorithm 1 is the most effecient algorithm out of the 
3 because it has the fastest runtime. 

Algorithm 1 has the fastest runtime because it uses a divide and conquer 
algorithm that splits the array into 3 and then just compares value

Algorithm 2 is in the middle becasue even though once it finds the median it is
faster than the other 2 finding the medain takes a while

Algorithm 3 has the slowest time because it sorts the array which takes a very
long time and is ineffiecent overall. 
'''

################################################################################