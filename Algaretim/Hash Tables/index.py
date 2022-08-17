"""HASH TABLES""" # ma'lumotlar tuzulmasi
"""hash tables nima: sizda mevalar ro'yxati bor (olma.15000 , banan 20000 siz olama desangiz kampyuter sizga O(1)tezligida olmani narxini qaytaradi sababi kampyuter olmani narxini yodlab olgan)"""
# misol uchun sizda sizda ro'yxatlar bor


# (tartibli ro'yxat)                    (tartibsiz ro'yxat)     
#                                   
#  1 anor = 20000                       1 limon = 12000
#  2 banan = 25000                      2 tarvuz = 12000
#  3 hurmo = 50000                      3 anor = 20000
#  4 limon = 12000                      4 hurmo = 50000
#  5 nok = 10000                        5 nok = 10000
#  6 tarvuz = 12000                     6 banan = 25000
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""HASH TABLES FUNKSIYA"""
# hash funksiya matinni takrorlanmas,noyob songa o'tkazib beradi
# noyob funksiyani turi ko'p
# yaxshi hash funksiyani belgilari (1.bir hil matn uchun bir hil son qaytaradi) (2.xar xil matnlar uchun xar xil son qaytaradi)
# hash funksiya sizga kerakli oraliqdagi sonlarni qaytaradi

# [bir xil matn uchun bir xil son qaytaradi]
# hashlarga misol: |_"olma"_| --> |_hash_| --> |_5_|

# [xar xil matn uchun xar xil son qaytaradi]
# hashlarga misol: |_"anor"_| --> |_hash_| --> |_0_|
# ---------------------------------------------------------------------------------------------------------------------------------------------
"""qanday hash jadval yaratamiz"""
# bizda ro'yxat bor
                                                            
#               ro'yxat                                      HASH                                   array
#                   1 anor = 20000              |_"anor"_| --> |_hash_| --> |_0_|               0 |_20 000_|   
#                   2 banan = 25000             |_"banan"_| --> |_hash_| --> |_2_|              1 |_50 000_|
#                   3 hurmo = 50000             |_"hurmo"_| --> |_hash_| --> |_1_|              2 |_25 000_|
#                   4 limon = 12000             |_"limon"_| --> |_hash_| --> |_5_|              3 |_12 000_|
#                   5 nok = 10000               |_"nok"_| --> |_hash_| --> |_4_|                4 |_10 000_|
#                   6 tarvuz = 12000            |_"tarvuz"_| --> |_hash_| --> |_3_|             5 |_12 000_|
# ------------------------------------------------------------------------------------------------------------------------

"""array jadvalidan qidirish""" 
#     
#   |_"hurmo"_| --> |_hash_| --> |_1_|        array                 hurmoni indexi 1 demak kapyuter arrayni 1 chisida turgan sonni chiqaradi
#                                           
#                                          0 |_20000_|        
#                                          1 |_50000_|
#                                          2 |_25000_|          <-- bu arrayni o'rnida bo'lishi shart emas buni o'rnida lugat yoki hash ni o'rnida yana bir hash boo'lishi mumkun.
#                                          3 |_12000_|
#                                          4 |_10000_|
#                                          5 |_12000_|
# ------------------------------------------------------------------------------------------------------------------------------------------

"""HASH TABLES"""
# eng foydali va ko'p ishlatiladigan ma'lumotlar tuzulmasi aksar dasturlash tillarida tadbiq qiling
# 1 hash maps
# 2 Dictionaries (python)
# -------------------------------------------------------------------------------------------------------

"""hash jadvallar qachon ishlatiladi"""
# misol uchun bizni kantaktlarimiz anna degan odamni ismini matn sifatida hash funsiyaga jo'natamiz shu odamni ma'lumotlarini jadvalda saqlaymiz
# -------------------------------------------------------------------------------------------------------------------------------------------------------

"""ma'lumotlar notekis tahsimlansa"""
# misol uchun siz anjirni narxini qidiryapsiz sizga 0 indexga ishora qiladi 0 index ga kirsangiz linked list ichidan bittalab qidirishingizga to'g'ri keladi va bu sizni qidirish vaqtingizga tasir qilishni boshlaydi
# ma'lumotlar notekis taqsimlansa ma'lum bir indexda linked list uzun bo'lib ketsa biz har bir linked listni ichini qarab chiqsak bizni qidiruv tizimimiz sekin ishlashni boshlaydi

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Big O"""


#                hash tables                   hash tables                         array                    linked list
#                (o'rtacha)                  (eng yomon holat)                      

#        ma'lumotlarni o'qish    O(1)               O(n)                            O(1)                            O(n)
#        ma'lumotlarni qo'shish  O(1)               O(n)                            O(n)                            O(1)
#        ma'lumotlarni o'chirish O(1)               O(n)                            O(n)                            O(1)