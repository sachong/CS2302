import random
"""

@author: Samuel Chong
CS2302
Olac Fuentes
Lab 2
Purpose: Sort lists using quick sort, merge sort and bubble sort and getting the median value


"""
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()     
    
def getLength(L):
    count = 0
    temp = L.head
    if L.head == None:
        return 0
    else:
        while temp is not None:
            count +=1
            temp = temp.next
        return count
            

def bubbleSort(L):
   count = 0
   sort = True
   while sort: #while sort is true
       temp = L.head
       sort = False
       while temp.next is not None:
           if temp.item > temp.next.item: #if the current item is greater than the next then swap position
               t = temp.item
               temp.item = temp.next.item
               temp.next.item = t
               count +=1
               sort = True #if something was swapped, then true
           temp = temp.next
           
           

def quickSort(L):
    count = 0
    if getLength(L) <= 1: #base case
        return L
    if getLength(L) > 1:
        pivot = L.head.item
        temp = L.head.next
        L1 = List()
        L2 = List()
        while(temp is not None): #after pivot
            if temp.item < pivot: #if item is less than the pivot, it goes to the small list
                Append(L1, temp.item)#insert n in L1
                count +=1
            else:
                Append(L2, temp.item)#insert n in L2
                count +=1
            temp = temp.next
        L1 = quickSort(L1) 
        L2 = quickSort(L2)
        Append(L1,pivot)
        L = addLists(L1,L2) #merge L1 and L2 into a single list
        return L
       

def addLists(L1,L2): # method to merge the lists for quick sort
    if(IsEmpty(L1)): #if list smaller than pivot is empty
        return L2
    elif(IsEmpty(L2)): #if list greater than pivot is empty
        return L1
    else:
        L1.tail.next = L2.head 
        L1.tail = L2.tail
        return L1
    
def modQuickSort(L,median):
    count = 0
    pivot = L.head.item
    temp = L.head.next
    L1 = List()
    L2 = List()
    while(temp is not None):
         if temp.item < pivot:#if item is less than the pivot, it goes to the small list
             Append(L1, temp.item)#insert n in L1
             count +=1
         else:
            Append(L2, temp.item)#insert n in L2
            count +=1
         temp = temp.next
    if getLength(L1) < median: #if median is not in L1, then search in L2
        count +=1
        return modQuickSort(L2,getLength(L1)-1)
    elif getLength(L2) < median: #if the median not in L2 
        count +=1
        return modQuickSort(L1,median)
    else: #if it isnt in L1 or L2
        return pivot
    
        
 

def sortList(l,r):
	result = None

	if l is None or getLength(l) < 1:
		return r
	if r is None or getLength(r) < 1:
		return l

	if l.head.item <= r.head.item:
		result = l.head
		temp = l.head.next
		tempL = List()
		tempL.head = temp
		result.next = sortList(tempL, r).head

	else:
		result = r.head
		temp = r.head.next
		tempL = List()
		tempL.head = temp
		result.next = sortList(l, tempL).head

	L = List()
	L.head = result
	return L


def mergeSort(L):
	if L is None or getLength(L)<2:
		return L

	mid = ElementAt(L,(getLength(L) // 2)-1)
	nextMid = mid.next

	mid.next = None

	left = mergeSort(L)
	R = List()
	R.head = nextMid
	right = mergeSort(R)

	sortedList = sortList(left, right)
	return sortedList
 
    
def sortList1(l,r):
	print("L: ")
	Print(l)
	print("R: ")
	Print(r)
	result = None

	if l is None or getLength(l) < 1:
		return r
	if r is None or getLength(r) < 1:
		return l

	if l.head.item <= r.head.item:
		result = l.head
		temp = l.head.next
		tempL = List()
		tempL.head = temp
		result.next = sortList(tempL, r).head

	else:
		result = r.head
		temp = r.head.next
		tempL = List()
		tempL.head = temp
		result.next = sortList(l, tempL).head

	L = List()
	L.head = result
	return L


def mergeSort1(L):
	Print(L)
	if L is None or getLength(L)<2:
		return L

	mid = ElementAt(L,(getLength(L) // 2)-1)
	nextMid = mid.next

	print("mid: ", mid.item)
	print("nextMid: ", nextMid.item)
	
	mid.next = None

	left = mergeSort(L)
	R = List()
	R.head = nextMid
	right = mergeSort(R)

	sortedList = sortList1(left, right)
	return sortedList

def Copy(L):
    copyList = List() #create new list
    temp = L.head
    while temp is not None:
        Append(copyList,temp.item) #add the item in temp everytime it iterates in the loop
        temp = temp.next
    return copyList
        
        
def ElementAt(L,n):
    if(getLength(L) < n): 
        return
    else:
        temp = L.head
        for i in range(n): #iterate n times
            temp = temp.next
        return temp
        

def Median(L):
    C = Copy(L)
    #bubbleSort(C)
    #quickSort(C)
    #mergeSort(C)
    #modQuickSort(C,getLength(L)//2)
    return ElementAt(C,getLength(C)//2)
       
L = List()

for i in range(5):
    randnum = random.randint(0,10)
    Append(L,randnum)
    
L1 =L


print("The original list is: ")
Print(L)
print()
'''
#BUBBLESORT
print("The median with bubble sort is: ")
bubbleSort(L)
medBubble = Median(L)
print(medBubble.item)

#MERGESORT
print("The median with merge sort is: ")
L=mergeSort(L)
medMerge = Median(L)
print(medMerge.item)
print()
'''

#QUICKSORT
print("The median with quick sort is: ")
L = quickSort(L)
medQuick = Median(L)
print(medQuick.item)
print()
'''

print("The median with modified quick sort is: ")
medModQuick = modQuickSort(L, getLength(L)//2)
medModQuick = Median(L)
print(medModQuick.item)
'''

print("The sorted list is: ")
Print(L)
    
