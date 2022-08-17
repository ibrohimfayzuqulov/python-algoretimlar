"""Graph ma'lumotlar tuzulmasi nima"""
# misol uchun xarita yoki navigator navigator bizga bizga o'zimiz turgan joydan boshlab bormoqchi bo'lgan joyimizga yo'lni bog'lab chizmalar bilan ko'rsatib berad huddi shu bo'g'lab ko'rsatish Graph deyiladi

# Graph ga misol:   

#   biz turgan joy <O> ________________
#                                      |                    (dunyo supermarketi)
#                                      |____________________________<0>_______________________________
#                                                                                                     |
#                                                                                                     |                   (bizni manzilimiz)
#                                                                                                     |_________________________<0>
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Graph qayerda ishlatiladi"""
# 1 Navigatsiya ( Google Maps,    Waze,    Yandex Maps)          <-- [Graph: sizga manzilingizga yo'lni chizmalar orqali ba boshqa narsalar orqali ko'rsatib beradi]
# 2 Aloqa tarmoqlarda                                            <-- [Graph: siz bir joydan ikkinchi joyga tel qilganingizda sizga eng yaqin aloqa tarmoqlari orqali ulashi kerak]
# 3 IP routing                                                   <-- [Graph: bir serverdan yakuniy foydalanuvchiga ma'lumotni yuborganda bir nechta yo'llardan borishi mumkun shu yerda xam eng tez yoki eng qisqa yo'lni topish kerak bo'ladi]
# 4 Ijtimoiy tarmoqlarda siz tanlaydigan odamlarni topishda      <-- [Graph: misol uchn siznig do'stingiz do'stingizni do'sti uni ukasi va otasi shunga va shunga o'xshash ma'lumotlar Graphlar ko'rinishida saqlanadi ]
# 5 Robot/Dron uchun yo'l topishda                               <-- [Graph: robotlar yoki ddronlar ular biror manzilga borish uchun ularga chizmali yo'l kerak bo'ladi ular xam Graph dan foydalanadi]       
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Graphlardan qanday ma'lumot qidirish mumkun""" # |
#                                                   v

"""BREADTH-FIRST SEARCH"""
# Breadth-first qidirish algoretimi Graph bilan ishlaydi
# ikki savolga javob beradi
#   1. A va B node orasida yo'l bormi?
#   2. A dan B ga eng yaqin yo'l qaysi
# --------------------------------------------------------------------------------------------

"""BREADTH-FIRST SEARCH qanday ishlaydi"""
# MISOL uchun siz elon musk ga aloqaga chiqmoqchisiz siz unga do'stlaringiz orqali bog'lanasiz oldin do'stlaringizni tekshirasiz elon musk sizni do'stingizni do'sti bo'lishi mumkun

# siz do'stlaringizni tekshirasiz va bu ("Queue") diyiladi