"""Quicksort"""
# tasaavvur qiling biz biror array elementini tartibga keltirmoqchimiz birinchi qiladigan ishimiz to'xtash sharti (base case) ni topish |
#                                                                                                                                       v
# to'xtash sharti ikki xil bo'lishi mumkun:
# 1 bosh array []
# 2 bir elementdan iborat array [9]
# 3 yuqoridagi ikki holda array tartibli bo'ladi unga misol |
#                                                           v
# def quicksort(array):
#   if len(array)<2:
#     return array
# -----------------------------------------------------------------------------------------------------------------------------------------------

"""agar array 2 elementdan iborat bo'lsa,tartiblash oson"""
# birinchi elementni 2-elemen bilan solishtiramiz va kerak bo'lsa o'rnini almashtiramiz: [12, 10] --> [10, 12]


"""agar array 3 ta elementdan iborat bo'lsachi"""
#       qsort ( |_22_|_22_|_20_|_5_| )

#       qsort ( |_20_|_5_| ) + |_22_| + qsort (25) --> |_5_|_20_|_22_|_25_|

#       qsort (|_5_|) + |_20_| -->  return |_5_|_20_|

# [uzunroq elementlar bilan ishlash]
# 
# qsort (|_22_|_34_|_20_|_5_|_44_|_6_|_12_|_9_|)
# 
# biz 12 ni tayanch qilib olamiz 12 dan kichik sonlarni chap tarfga katta sonlarni  o'ng tarafga qo'yib
# -----------------------------------------------------------------------------------------------------------
"""Quicksort algoritimi tez ishlash uchun tayanch elementni tasidifiy olgan afzal (aks holda Bog O qiymati O(n2)bo'lishi mumkun)"""
# umuman olganda esa quicksort uchun Big O: O(nlogn)
# [quicksort funksiyasi]
from array import array
from random import randrange
from re import I
def qsort(array):
    if len(array)<2:   # to'xtash sharti    
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        kichik =  [i for i in array if i<=pivot]
        katta =  [i for i in array if i>pivot ]
        print(f"{kichik}+[{pivot}]+{katta}")
        return qsort(kichik) + [pivot] + qsort(katta)

if __name__ == '__main__':
    array1 = [1,5,12,0,-5,66]
    print(array1)
    print(qsort(array1))
    array2 = list(range(20))
    print(array2)
    print(qsort(array2))