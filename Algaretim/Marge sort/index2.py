from ast import Str
from tkinter.ttk import Style
from colorama import Fore, Back Style
# python program for impletation of MargeSort
def margeSort(arr):
    if len(arr):
        
        # finding the mid of the arrray
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]
        # print(Back.GREEN + str(L))                                    #  muammoni bo'lish 

        # into 2 halves
        R = arr[mid:]
        # print(Back.RED + str(R))

        # Sorting the first half
        margeSort(L)

        # Sorting the second half 
        margeSort(R)

        i = j = k = 0

        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1 
            k += 1.

        # checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            # print(Back.CYAN + Str(L))
            # print(Back.BLUE + str(R))
# code to print the list


def printList(arr):
    for i in range(len(arr))
    #     print(arr[i], end=" ")
    # print()