#PROGRAM TOL

#LIST, FUNGSI, DLL

daftar_g_tol = [
    [1, 'Merak'],
    [2, 'Tangerang'],
    [3, 'Jakarta'],
    [4, 'Cikampek'],
    [5, 'Cikopo'],
    [6, 'Palimanan'],
    [7, 'Kanci'],
    [8, 'Pejagan'],
    [9, 'Pemalang'],
    [10, 'Batang'],
    [11, 'Semarang (Kaliangkung)'],
    [12, 'Semarang ABC'],
    [13, 'Solo']
]

def title():
    print("")
    print(("="*18).center(43))
    print("ESTIMASI TARIF TOL".center(43))
    print("JAKARTA-SOLO".center(43))
    print(("="*18).center(43))

def tabel():
    print("")
    print("{}{:^6}{}{:^34}{}".format("|", "-"*6, "|", "-"*34, "|"))
    print("{}{:^6}{}{:^34}{}".format("|", "Kode", "|", "Kota", "|"))
    print("{}{:^6}{}{:^34}{}".format("|", "-"*6, "|", "-"*34, "|"))
    for i in range(len(daftar_g_tol)):
        nnn_kode = daftar_g_tol[i][0]
        nnn_kota = daftar_g_tol[i][1]
        isi = "{}{:^6}{}{:^34}{}".format("|", nnn_kode, "|", nnn_kota, "|")
        print(isi)
    print("{}{:^6}{}{:^34}{}".format("|", "-"*6, "|", "-"*34, "|"))

def format_estimasi():
    print(("="*18).center(43))
    print("ESTIMASI TARIF TOL".center(43))
    print(("="*18).center(43))

#PROGRAM UTAMA
title()

print("")
print("Masukkan kode kota asal dan kode kota")
print("tujuan anda berdasarkan tabel di bawah !")

tabel()
print("")

kota_asal = int(input("Masukkan kode kota asal anda : "))
kota_tujuan = int(input("Masukkan kode kota tujuan anda : "))
print("")

#PERCABANGAN 1 (sesuai data)

#tangerang-merak
if kota_asal == 1 and kota_tujuan == 2 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 44.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 1 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 44.000 ,-".center(43))
    print("")

#tangerang-jkt
elif kota_asal == 3 and kota_tujuan == 2 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 8.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 3 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 8.000 ,-".center(43))
    print("")

#merak-jkt
elif kota_asal == 1 and kota_tujuan == 3 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 52.000 ,-".center(43))
    print("")
elif kota_asal == 3 and kota_tujuan == 1 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 52.000 ,-".center(43))
    print("")

#jkt-cikampek
elif kota_asal == 3 and kota_tujuan == 4 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 36.000 ,-".center(43))
    print("")
elif kota_asal == 4 and kota_tujuan == 3 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 36.000 ,-".center(43))
    print("")

#cikampek-cikopo
elif kota_asal == 5 and kota_tujuan == 4 :
    print("Kota asal   : Cikopo")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 40.000 ,-".center(43))
    print("")
elif kota_asal == 4 and kota_tujuan == 5 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Cikopo")
    print("")
    format_estimasi()
    print("Rp. 40.000 ,-".center(43))
    print("")

#palimanan-cikopo
elif kota_asal == 5 and kota_tujuan == 6 :
    print("Kota asal   : Cikopo")
    print("Kota tujuan : Palimanan")
    print("")
    format_estimasi()
    print("Rp. 119.000 ,-".center(43))
    print("")
elif kota_asal == 6 and kota_tujuan == 5 :
    print("Kota asal   : Palimanan")
    print("Kota tujuan : Cikopo")
    print("")
    format_estimasi()
    print("Rp. 119.000 ,-".center(43))
    print("")

#palimanan-kanci
elif kota_asal == 7 and kota_tujuan == 6 :
    print("Kota asal   : Kanci")
    print("Kota tujuan : Palimanan")
    print("")
    format_estimasi()
    print("Rp. 13.000 ,-".center(43))
    print("")
elif kota_asal == 6 and kota_tujuan == 7 :
    print("Kota asal   : Palimanan")
    print("Kota tujuan : Kanci")
    print("")
    format_estimasi()
    print("Rp. 13.000 ,-".center(43))
    print("")

#kanci-pejagan
elif kota_asal == 7 and kota_tujuan == 8 :
    print("Kota asal   : Kanci")
    print("Kota tujuan : Pejagan")
    print("")
    format_estimasi()
    print("Rp. 30.000 ,-".center(43))
    print("")
elif kota_asal == 8 and kota_tujuan == 7 :
    print("Kota asal   : Pejagan")
    print("Kota tujuan : Kanci")
    print("")
    format_estimasi()
    print("Rp. 30.000 ,-".center(43))
    print("")

#pemalang-pejagan
elif kota_asal == 9 and kota_tujuan == 8 :
    print("Kota asal   : Pemalang")
    print("Kota tujuan : Pejagan")
    print("")
    format_estimasi()
    print("Rp. 60.000 ,-".center(43))
    print("")
elif kota_asal == 8 and kota_tujuan == 9 :
    print("Kota asal   : Pejagan")
    print("Kota tujuan : Pemalang")
    print("")
    format_estimasi()
    print("Rp. 60.000 ,-".center(43))
    print("")

#pemalang-batang
elif kota_asal == 9 and kota_tujuan == 10 :
    print("Kota asal   : Pemalang")
    print("Kota tujuan : Batang")
    print("")
    format_estimasi()
    print("Rp. 45.000 ,-".center(43))
    print("")
elif kota_asal == 10 and kota_tujuan == 9 :
    print("Kota asal   : Batang")
    print("Kota tujuan : Pemalang")
    print("")
    format_estimasi()
    print("Rp. 45.000 ,-".center(43))
    print("")

#semarang-batang
elif kota_asal == 11 and kota_tujuan == 10 :
    print("Kota asal   : Semarang (Kaliangkung)")
    print("Kota tujuan : Batang")
    print("")
    format_estimasi()
    print("Rp. 86.000 ,-".center(43))
    print("")
elif kota_asal == 10 and kota_tujuan == 11 :
    print("Kota asal   : Batang")
    print("Kota tujuan : Semarang (Kaliangkung)")
    print("")
    format_estimasi()
    print("Rp. 86.000 ,-".center(43))
    print("")

#semarang-semarang abc
elif kota_asal == 11 and kota_tujuan == 12 :
    print("Kota asal   : Semarang (Kaliangkung)")
    print("Kota tujuan : Semarang ABC")
    print("")
    format_estimasi()
    print("Rp. 6.000 ,-".center(43))
    print("")
elif kota_asal == 12 and kota_tujuan == 11 :
    print("Kota asal   : Semarang ABC")
    print("Kota tujuan : Semarang (Kaliangkung)")
    print("")
    format_estimasi()
    print("Rp. 6.000 ,-".center(43))
    print("")

#SOLO-semarang abc
elif kota_asal == 13 and kota_tujuan == 12 :
    print("Kota asal   : Solo")
    print("Kota tujuan : Semarang (ABC)")
    print("")
    format_estimasi()
    print("Rp. 75.000 ,-".center(43))
    print("")
elif kota_asal == 12 and kota_tujuan == 13 :
    print("Kota asal   : Semarang (ABC)")
    print("Kota tujuan : Solo")
    print("")
    format_estimasi()
    print("Rp. 75.000 ,-".center(43))
    print("")

#PERCABANGAN 2 (kota asal merak)
elif kota_asal == 1 and kota_tujuan == 4 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 88.000 ,-".center(43))
    print("")
elif kota_asal == 4 and kota_tujuan == 1 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 88.000 ,-".center(43))
    print("")
elif kota_asal == 1 and kota_tujuan == 5 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Cikopo")
    print("")
    format_estimasi()
    print("Rp. 128.000 ,-".center(43))
    print("")
elif kota_asal == 5 and kota_tujuan == 1 :
    print("Kota asal   : Cikopo")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 128.000 ,-".center(43))
    print("")
elif kota_asal == 1 and kota_tujuan == 6 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Palimanan")
    print("")
    format_estimasi()
    print("Rp. 247.000 ,-".center(43))
    print("")
elif kota_asal == 5 and kota_tujuan == 1 :
    print("Kota asal   : Palimanan")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 247.000 ,-".center(43))
    print("")
elif kota_asal == 1 and kota_tujuan == 7 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Kanci")
    print("")
    format_estimasi()
    print("Rp. 260.000 ,-".center(43))
    print("")
elif kota_asal == 7 and kota_tujuan == 1 :
    print("Kota asal   : Kanci")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 260.000 ,-".center(43))
    print("")
elif kota_asal == 1 and kota_tujuan == 8 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Pejagan")
    print("")
    format_estimasi()
    print("Rp. 290.000 ,-".center(43))
    print("")
elif kota_asal == 8 and kota_tujuan == 1 :
    print("Kota asal   : Pejagan")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 290.000 ,-".center(43))
    print("")
elif kota_asal == 1 and kota_tujuan == 9 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Pemalang")
    print("")
    format_estimasi()
    print("Rp. 350.000 ,-".center(43))
    print("")
elif kota_asal == 9 and kota_tujuan == 1 :
    print("Kota asal   : Pemalang")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 350.000 ,-".center(43))
    print("")
elif kota_asal == 1 and kota_tujuan == 10 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Batang")
    print("")
    format_estimasi()
    print("Rp. 395.000 ,-".center(43))
    print("")
elif kota_asal == 10 and kota_tujuan == 1 :
    print("Kota asal   : Batang")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 395.000 ,-".center(43))
    print("")
elif kota_asal == 1 and kota_tujuan == 11 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Semarang (Kaliangkung)")
    print("")
    format_estimasi()
    print("Rp. 401.000 ,-".center(43))
    print("")
elif kota_asal == 11 and kota_tujuan == 1 :
    print("Kota asal   : Semarang (Kaliangkung)")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 401.000 ,-".center(43))
    print("")
elif kota_asal == 1 and kota_tujuan == 12 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Semarang (ABC)")
    print("")
    format_estimasi()
    print("Rp. 407.000 ,-".center(43))
    print("")
elif kota_asal == 12 and kota_tujuan == 1 :
    print("Kota asal   : Semarang (ABC)")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 407.000 ,-".center(43))
    print("")
elif kota_asal == 1 and kota_tujuan == 13 :
    print("Kota asal   : Merak")
    print("Kota tujuan : Solo")
    print("")
    format_estimasi()
    print("Rp. 482.000 ,-".center(43))
    print("")
elif kota_asal == 13 and kota_tujuan == 1 :
    print("Kota asal   : Solo")
    print("Kota tujuan : Merak")
    print("")
    format_estimasi()
    print("Rp. 482.000 ,-".center(43))
    print("")

#PERCABANGAN 3 (kota asal tangerang)
#cikampek-tangerang
elif kota_asal == 4 and kota_tujuan == 2 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 44.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 4 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 44.000 ,-".center(43))
    print("")

#cikopo-tangerang
elif kota_asal == 5 and kota_tujuan == 2 :
    print("Kota asal   : Cikopo")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 84.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 5 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Cikopo")
    print("")
    format_estimasi()
    print("Rp. 84.000 ,-".center(43))
    print("")

#palimanan-tangerang
elif kota_asal == 6 and kota_tujuan == 2 :
    print("Kota asal   : Palimanan")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 203.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 6 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Palimanan")
    print("")
    format_estimasi()
    print("Rp. 203.000 ,-".center(43))
    print("")

#kanci-tangerang
elif kota_asal == 7 and kota_tujuan == 2 :
    print("Kota asal   : Kanci")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 216.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 7 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Kanci")
    print("")
    format_estimasi()
    print("Rp. 216.000 ,-".center(43))
    print("")

#pejagan-tangerang
elif kota_asal == 8 and kota_tujuan == 2 :
    print("Kota asal   : Pejagan")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 246.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 8 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Pejagan")
    print("")
    format_estimasi()
    print("Rp. 246.000 ,-".center(43))
    print("")

#pemalang-tangerang
elif kota_asal == 9 and kota_tujuan == 2 :
    print("Kota asal   : Pemalang")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 306.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 9 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Pemalang")
    print("")
    format_estimasi()
    print("Rp. 306.000 ,-".center(43))
    print("")

#batang-tangerang
elif kota_asal == 10 and kota_tujuan == 2 :
    print("Kota asal   : Batang")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 351.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 10 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Batang")
    print("")
    format_estimasi()
    print("Rp. 351.000 ,-".center(43))
    print("")

#semarang kali-tangerang
elif kota_asal == 11 and kota_tujuan == 2 :
    print("Kota asal   : Semarang (Kaliangkung)")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 437.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 11 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Semarang (Kaliangkung)")
    print("")
    format_estimasi()
    print("Rp. 437.000 ,-".center(43))
    print("")

#semarang abc-tangerang
elif kota_asal == 12 and kota_tujuan == 2 :
    print("Kota asal   : Semarang (ABC)")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 443.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 12 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Semarang (ABC)")
    print("")
    format_estimasi()
    print("Rp. 443.000 ,-".center(43))
    print("")

#solo-tangerang
elif kota_asal == 13 and kota_tujuan == 2 :
    print("Kota asal   : Solo")
    print("Kota tujuan : Tangerang")
    print("")
    format_estimasi()
    print("Rp. 518.000 ,-".center(43))
    print("")
elif kota_asal == 2 and kota_tujuan == 13 :
    print("Kota asal   : Tangerang")
    print("Kota tujuan : Solo")
    print("")
    format_estimasi()
    print("Rp. 518.000 ,-".center(43))
    print("")

#PERCABANGAN 4 (kota asal jkt)
#jkt-cikopo
elif kota_asal == 3 and kota_tujuan == 5 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Cikopo")
    print("")
    format_estimasi()
    print("Rp. 76.000 ,-".center(43))
    print("")
elif kota_asal == 5 and kota_tujuan == 3 :
    print("Kota asal   : Cikopo")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 76.000 ,-".center(43))
    print("")

#jkt-palimanan
elif kota_asal == 3 and kota_tujuan == 6 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Palimanan")
    print("")
    format_estimasi()
    print("Rp. 195.000 ,-".center(43))
    print("")
elif kota_asal == 6 and kota_tujuan == 3 :
    print("Kota asal   : Palimanan")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 195.000 ,-".center(43))
    print("")

#jkt-kanci
elif kota_asal == 3 and kota_tujuan == 7 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Kanci")
    print("")
    format_estimasi()
    print("Rp. 208.000 ,-".center(43))
    print("")
elif kota_asal == 7 and kota_tujuan == 3 :
    print("Kota asal   : Kanci")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 208.000 ,-".center(43))
    print("")

#jkt-pejagan
elif kota_asal == 3 and kota_tujuan == 8 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Pejagan")
    print("")
    format_estimasi()
    print("Rp. 268.000 ,-".center(43))
    print("")
elif kota_asal == 8 and kota_tujuan == 3 :
    print("Kota asal   : Pejagan")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 268.000 ,-".center(43))
    print("")

#jkt-pemalang
elif kota_asal == 3 and kota_tujuan == 9 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Pemalang")
    print("")
    format_estimasi()
    print("Rp. 328.000 ,-".center(43))
    print("")
elif kota_asal == 9 and kota_tujuan == 3 :
    print("Kota asal   : Pemalang")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 328.000 ,-".center(43))
    print("")

#jkt-batang
elif kota_asal == 3 and kota_tujuan == 10 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Batang")
    print("")
    format_estimasi()
    print("Rp. 373.000 ,-".center(43))
    print("")
elif kota_asal == 10 and kota_tujuan == 3 :
    print("Kota asal   : Batang")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 373.000 ,-".center(43))
    print("")

#jkt-semarang kali
elif kota_asal == 3 and kota_tujuan == 11 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Semarang (Kaliangkung)")
    print("")
    format_estimasi()
    print("Rp. 459.000 ,-".center(43))
    print("")
elif kota_asal == 11 and kota_tujuan == 3 :
    print("Kota asal   : Semarang (Kaliangkung)")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 459.000 ,-".center(43))
    print("")

#jkt-semarang abc
elif kota_asal == 3 and kota_tujuan == 12 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Semarang (ABC)")
    print("")
    format_estimasi()
    print("Rp. 465.000 ,-".center(43))
    print("")
elif kota_asal == 12 and kota_tujuan == 3 :
    print("Kota asal   : Semarang (ABC)")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 465.000 ,-".center(43))
    print("")

#jkt-solo
elif kota_asal == 3 and kota_tujuan == 13 :
    print("Kota asal   : Jakarta")
    print("Kota tujuan : Semarang (ABC)")
    print("")
    format_estimasi()
    print("Rp. 540.000 ,-".center(43))
    print("")
elif kota_asal == 13 and kota_tujuan == 3 :
    print("Kota asal   : Semarang (ABC)")
    print("Kota tujuan : Jakarta")
    print("")
    format_estimasi()
    print("Rp. 540.000 ,-".center(43))
    print("")

#CABANG 4 (kota asal cikampek)
#cikampek-palimanan
elif kota_asal == 4 and kota_tujuan == 6 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Palimanan")
    print("")
    format_estimasi()
    print("Rp. 159.000 ,-".center(43))
    print("")
elif kota_asal == 6 and kota_tujuan == 4 :
    print("Kota asal   : Palimanan")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 159.000 ,-".center(43))
    print("")

#cikampek-kanci
elif kota_asal == 4 and kota_tujuan == 7 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Kanci")
    print("")
    format_estimasi()
    print("Rp. 172.000 ,-".center(43))
    print("")
elif kota_asal == 7 and kota_tujuan == 4 :
    print("Kota asal   : Kanci")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 172.000 ,-".center(43))
    print("")

#cikampek-kanci
elif kota_asal == 4 and kota_tujuan == 8 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Pejagan")
    print("")
    format_estimasi()
    print("Rp. 202.000 ,-".center(43))
    print("")
elif kota_asal == 8 and kota_tujuan == 4 :
    print("Kota asal   : Pejagan")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 202.000 ,-".center(43))
    print("")

#cikampek-pejagan
elif kota_asal == 4 and kota_tujuan == 9 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Pejagan")
    print("")
    format_estimasi()
    print("Rp. 262.000 ,-".center(43))
    print("")
elif kota_asal == 9 and kota_tujuan == 4 :
    print("Kota asal   : Pejagan")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 262.000 ,-".center(43))
    print("")

#cikampek-pemalang
elif kota_asal == 4 and kota_tujuan == 10 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Pemalang")
    print("")
    format_estimasi()
    print("Rp. 407.000 ,-".center(43))
    print("")
elif kota_asal == 10 and kota_tujuan == 4 :
    print("Kota asal   : Pemalang")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 407.000 ,-".center(43))
    print("")

#cikampek-batang
elif kota_asal == 4 and kota_tujuan == 11 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Batang")
    print("")
    format_estimasi()
    print("Rp. 493.000 ,-".center(43))
    print("")
elif kota_asal == 11 and kota_tujuan == 4 :
    print("Kota asal   : Batang")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 493.000 ,-".center(43))
    print("")

#cikampek-KALI
elif kota_asal == 4 and kota_tujuan == 12 :
    print("Kota asal   : Cikampek")
    print("Kota tujuan : Semarang(Kaliangkung)")
    print("")
    format_estimasi()
    print("Rp. 579.000 ,-".center(43))
    print("")
elif kota_asal == 12 and kota_tujuan == 4 :
    print("Kota asal   : Semarang(Kaliangkung)")
    print("Kota tujuan : Cikampek")
    print("")
    format_estimasi()
    print("Rp. 579.000 ,-".center(43))
    print("")

#cikampek- semarang ABC


else:
    print("Input belom terdaftar")