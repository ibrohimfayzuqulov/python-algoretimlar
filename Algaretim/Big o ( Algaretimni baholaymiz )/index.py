def linear_search(list, item):
    for n  in range(len(list)):
        if list[n]==item:
            return n
        return None
def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        return None
# --------------------------------------------------------------------------------------------
# [ tartibli ro'yxat ]
# myList1 = [1,2,4,6,7,10,12,15,18,21,24]
# print(linear_search(myList1,10))
# print(binary_search(myList1,10))
# --------------------------------------------------------------------------------------------

# [ tartibsiz ro'yxat ]
# myList2 = [18,12,25,1,3,4,10,5,23,4,13,89]
# myList2.sort()
# print(linear_search(myList2,13))
# print(binary_search(myList2,13))
# --------------------------------------------------------------------------------------------
# # [ matnlar bilan ishlash ]
# mevalar = ['olma','anor','olcha','behi','shaftoli','gulos']
# mevalar.sort()
# print(mevalar)
# print(binary_search(mevalar,'olma'))
# --------------------------------------------------------------------------------------------
""" Big O nima"""
# Big O (katta O) - algaretimni tezligini o'lchash uchun mezon
# Big O eng yomon holatdagi tezlikni o'lchaydi
# O buyerda o'lchov birligi (aperatsiyalar soni)
# -------------------------------------------------------------------------------------------

"""Bazi algaretimlarni tezligi"""
# O(log2n)-Binary search  <--  [eng tezi]
# O(n)-Linear search
# O(n2)-Slow sorting Algorithm
# O(n!)-Traveling salesperson