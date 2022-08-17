""" rekursiyaga misol"""
# 1 misol bir quti ni ichidan kalit ni olmoqchisiz va qutini ochdingiz agar kalitni topsangiz qidirishni to'xtatamiz
# 2 misol uchun bir quti ichidan kalit topmoqchisiz qutini ochdingiz karasangiz qutini ichida yana bir quti bor siz nima qilasiz qutini ichidagiz qutini ochishingiz rekursiya deyiladi
# (WHILE VA RECURSION BIR XIL NAYIJA BERADI FAQAT RECURSION TARTIBLIROQ VA KAMROQ KOD ISHLATILADI
# --------------------------------------------------------------------------------------------------------------------

"""while ga misol"""

# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()              
#     while pile is not empty:
#         box = pile.grap_a_box()                                           2 KALASI BIR XIL NATIJA BERADI      
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print "found the key!"

#---------------------------------------------------------------------------------------

"""rekursiya ga misol"""
# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)# <- recursion!
#         elif item.is_a_key():
#             print "found the key"

# ---------------------------------------------------------------------------------------------------------------
"""10DAN 1 GACHA SANASH""" 
#                        def sana(n):
#                            print(n)
#  to'xtash sharti -->       if n<=1:
#                               return
#  rekursiya  sharti -->     elif:
#                               sana(n-1)
# -----------------------------------------------------------------------------------------------------

def sana(n):
    print(n)
    if n<=1:
        return
    else:
        sana(n-1)