"""Dijkstra algoretimi vaznli graflarda 'eng arzon' yo'lni topish uchun  ishlatiladi"""
# masofa
# narx
# vaqt
# vazn
# va boshqa narsalar
# -------------------------------------------------------------------------------------------------------
"""dijkstra algoretimi qanday ishlaydi"""
# [bizda tugunlar bor toshkentga borish uchun yo'lni va boshqa narsalarni ko'rsatadi]
# boshlang'ich tugundan borish mumkun bo'lgan "eng arzon" tugunni topamiz
# eng arzon tugun qo'shnilarnig "narxini" topamiz
# yuqoridagi qadamni barcha tugunlar uchun takrorlaymiz
# yakuniy yo'lni toping
# -----------------------------------------------------------------------------------------------------

# Dijkstra algoretimi faqat yo'naltirilgan ACYCLIC graphlar bilan ishlaydi

# Dijkstra algoretimi manfiy vazinli Graphlar bilan ishlamaydi

# yo'naltirilmagan graph (cyclic garph) deyiladi
# -------------------------------------------------------------------------------------------------------------

"""Breadth-First  VS  Dijkstra"""

# Breadth-First

# bosh tugundan oxiri tugungacha barcha tugunlarni ko'rib chiqadi
# faqatgina vazin (yoki bir hil vazin) graphlar bilan ishlaydi
# nayija: "eng qisqa" yo'l
# Big O: O(N+E)
# ---------------------------------------------------------

# Dijkstra

# harv qadamda eng arzon tugunga o'tadi
# musbat vazinli va vazinsiz graphlar bilan ishlaydi
# natija: "eng arzon" yo'l
# Big O: O(N+E(LogN))

# ----------------------------------------------------------

# manfiy vazinli graphlar uchun BILLMAN-FORD ALORETIMNI KO'RIG