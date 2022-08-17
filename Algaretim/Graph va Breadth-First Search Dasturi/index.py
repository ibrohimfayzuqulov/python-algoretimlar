"""Graphni dasturlash"""

# [yo'naltirilgan Graph (directed graph)]
# misol uchun siz (intagram) yoki (you tube) da bir odamni kuzatsib borasiz leki u sizni kuzatmaydi. shu yo'naltirilgan Graph diyiladi. bog'lanish bir tomonlama. tohir umed ni taneydi lekin umed tohirni tanimaydi
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# [yo'naltirilmagan Graph (undirected graph)]
# bu ikkala tugun xam bir biriga bog'langan tohir umedni taneydi umed ham tohirni taneydi bunda birinchi tugundan ikkinchi tugunga yo'l bor
# ----------------------------------------------------------------------------------------------------------------------------------------------------

"""pythonda graphlarni dictionary (lug'at,hash jadvali) yordamida yaratish mumkun"""

graph = {} # bo'sh graph
graph['siz'] = ['ali','vali','tohir'] #Graph tugunlari
# --------------------------------------------------------------------------------------------------------------------------------------------

"""Algoretimni qidirish"""
# 1-qadam: Queue  yaratamiz     -->                      |_Ali_|_Vali_|_Tohir_|

# 2-qadam: Queue boshidagi odamni ajratamiz           |_Ali_|  |_Vali_|_Tohir_|

# 3-qadam: tekshiramiz Ali ilon musk mi yoki yo'q ?      |_Ali_| == |_Elon Musk_|

#                                                         ^
# 4-qadam: Natijaga qarab ish ko'ramiz ( --> bu yerda ikkta natija bo'lishi mumkun agar | ali Elon Musk ga teng bo'lsa biz qidirishni to'xtatamiz lekin bu yerda ali elon musk emas )

# 5-qadam: Loop

# 6-qadam: agar elon musk topilmasa , demak unga bog'lana olmaymiz



# ------------------------------>> kodi index2.py da