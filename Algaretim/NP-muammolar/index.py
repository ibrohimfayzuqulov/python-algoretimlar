from importlib.abc import Traversable


"""Traveling salesperson problem"""
# Np-miammoni belgilari  (NP MUAMMOLARGA OCHKO'Z ALGORETIMLAR BILAN YECHIM TOPSAK BO'LADI)
# 1 kichik sonlar uchun tez katta sonlar uchun juda sekin ishlaydigan muammolar
# 2 X ning barcha kombinatsiyalarinii toping mazmunidagi muammolar
# 3 har bir yechimni ko'rib chiqish kerak bo'lgan muammolar
# 4 ketma-ketliklarni qarab chiqish talab qilinadigan muammolar huddi (musofir muammosi kabi)
# 5 barcha to'plamlarni ko'rib chiqish talab qilinadigan muammolar
# [musofir muammosi]
# 1 savdogar ish bilan safarga chiqdi va safar davomida 5ta manzilga kirib o'tishi kerak.
# 2 muammo: 5ta manzilga eng kam vaqt (yoki masofa) bosib  kirib o'tish yo'lini topish