"""stack bu qanaydir buyumlarni yoki hujjatlarni ustma ust tahlanishi"""
# LIFO MA'LUMOTLAR TO'PLAMI
# LIFO (List In First Out) - oxirgi kirgan birinchi chiqadi
# ma'kumotlar to'plami ustiga qo'shiladi va to'plam ustidan olinadi
# misol: 
#       |_6_|
#       |_5_|       (birinchi kirgan ma'lumot oxirda bo'adi) (oxiri kirgan ma'lumot birinchida turadi)
#       |_4_|
#       |_3_|
#       |_2_|       (telefondagi sms ni ham misol qilib keltirsak bo'ladi birinchi kelgan sms pastda oxirida bo'ladi.. oxiri kelgan ma'lumot 1 da)
#       |_1_|
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

"""the stack ustidagi amallar"""
# 1 push = element qo'shish
# 2 pop = elementni sug'urib olish
# 3 isEmpty = to'plam bo'sh ekanligini tekshirish
# 4 isFull = to'plam to'la ekanligini tekshirish
# 5 peek = eng yuqoridagi element qiymatini ko'rish