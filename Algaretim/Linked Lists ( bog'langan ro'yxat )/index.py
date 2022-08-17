"""Linked Lists"""
# Linked Lists ham aslida array ga o'shqab bir nechta ro'yxatlarni saqlaydigan ro'yxat
# LINKED LISTS - bu ketma ketligi xotiradagi  joylashuvga bog'liq bo'lmagan chiziqli ma'lumotlar to'plami   
# ro'yxatni har bir elementi keyingi elementga ishora qiladi.
# ma'lumolar tuzulmasi sifatida LL ni bir biriga bog'langan tugunlar ko'rinshida tasvvur qilamiz
# har bir tugun o'z qiymatini va keyingi element manzilini saqlaydi(misol |)
#                                                                         v   
# |_A_|__|  ->  |_B_|__|  ->  |_C_|__|  ->  |_D_|__|  ->  |_E_|__|  ->  |__|

# ARRAY - xotirada har bir element ketmaket joylashgan bo'ladi.
# LINKED LISTS - da esa istalgan  joyga joylashaveradi bo'sh joy bo'lsa bo'ldi
# misol uchun siz 1000 ta element olib kelmoqchisiz lekin xotirada 1000 ta elementga joy yo'q siz 1000 ta elementni 500 tasini olib kelishingiz mumkun yani xotirada nechta elementga joy bor ushancha elementni olib kelishingiz mumkun
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Biz u qiyymatlarni qanday qilib topamiz""" 
# manzil orqali  biz 1 chi elementni manzilini bilamiz keyin 1 elementdan 2 ga 2 chi elementdan 3 ga 3 dan 4 chi elementlarga shunday qilib o'tamiz
# ---------------------------------------------------------------------------------------------------------------------------------------------------------

"""element qo'shish"""
# biror bir elemen qo'shib manzilni o'sha yangi elementga bog'lab qo'yasiz (bu arraydan ancha tezroq bo'ladi)
# -----------------------------------------------------------------------------------------------------------------

"""linked listsni afzaliklari"""
# 1 tez yozish va o'chirish
# 2 o'zgaruvchat hajmga ega
# 3 xotiradan samarali foydalanish
# --------------------------------------------
"""linked lists kamchiliigi"""
# 1 sekin qidirish
# 2 har bir tugun xotirada  ko'proq joy egallaydi sababbi (har bitta tugun oz'ini qiymatini saqlaydi ha keyingi tugunni mazilini saqlaydi.)
# arrayni istalgan joyidan ma'lumot o'qish 1 ta aperatsiya talab qiladi. (sababi arraylar indexlangan shu uchun arrayni o'qish juda tez)
# linked lists da esa biz faqat bitta manzilni bilamiz shu uchun hammaa elementlarni bittalb o'qib chiqishimizga to'g'ri keladi ( a,dan b,ga b,dan c,ga c,dan d ga o'tamiz)
# lekin 'Linked lists' 'array' ga qaraganda elementlarni qo'shish da o'chirishda tezoq ishlaydi
# --------------------------------------------------------------------------------------------------------------------------------------------------------

"""Linked lists turlari"""
# [singly linked lists- (bir tomonlama ro'yxat)]
# 1 bir tomonlama ro'yxat 1 element kiyingi elementga bog'langan bo'ladi (oxirgi element hech qayerga ishora qilmaydi)  
# [circular linked lists (aylana ro'yxat)]
# 2 oxirgi element birinchi elenrga ishora ilib turadi yani oxirgi elementda 1 chi elementni manzili turadi
# [Doubly linked lists (ikki tomonlama ro'yxat)]
# har bitta tugun avvalgi va kiyingi tugun manzilini saqlaydi  (bu xotirada yana qo'shimcha joy egallaydi sababi 1ta tugun ham o'zidan oldingi va kiyigi tugun manzilini saqlaydi)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""ABSTRAKT MA'LUMOTLAR TURLARI"""
# ma'lumotalar turiga dasturlash tilidan uzulgan holda qarash
# Abstrakt ma'lumot turi u saqlaydigan qiymatlar va uning ustida bajarish mumkun bo'lgan operatsiyalar bilan aniqlanadi



