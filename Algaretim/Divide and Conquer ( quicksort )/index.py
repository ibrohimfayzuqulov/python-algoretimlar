"""Quicksort"""
# Quicksort ham selection sort kabi ma'lumotlarni tartiblash uchun ishlatiladi 'Quicksort' dan bir necha barobar tezroq bo'lgan algaretim
# -----------------------------------------------------------------------------------------------------------------------------------------------

"""DIVIDE & CONQUER (bo'lib tashla va hukumronlik qil)"""
# bazida muammolarga yechim ko'rinmaydi .
# shu payt katta muammolarni mayda muammolarga bo'lib olib, har bir muammoni alohida hal qiladi va shu narsa (divide and conquer metodi deb ataladi)
# Divide and conquer metodi juda ko'p muammolarga yechim bo'lishi mumkun.
# keyingi safar murakkab muammoga to'qnash kelganigizda shu metodni esga soling
# rekursiyani har bir qadami bilan muammo kichrayib borishi kerak
# -----------------------------------------------------------------------------------------------------------------
# misol uchun bizda array elementlari yig'indisini hisoblang [5,8,12,22]
#   1 to'xtash shartini aniqlaymiz
#   2 to'xtash shartiga yetish uchun har qadamda muammoni kichraytirish yo'lini topamiz
# 
#  [''to'xtash shartini aniqlaymiz]
# misol uchun bizda raqamlar bor |_5_|_8_|_12_|_22_| yoki element yo'q
# agar arrayda 1ta element bo'lsa shu elementni qaytaramiz
# agar arrayda element bo'lmasa O qaytaramiz 
# ['to'xtash shartiga yetish uchun' har qandamda muammoni kichraytirish yo'lini topamiz]
# har qadamda O ta elementdan iborat arrayga yaqinlashamiz buni qanday qilamiz |
#                                                                              v
# berilgan array elementlari yig'indisi hisoblang:[5,8,12,22]
# sum(|_5_|_8_|_12_|_22_|)