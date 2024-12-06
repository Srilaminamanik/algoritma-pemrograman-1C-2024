# a. Membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang
klub_basket = set()
klub_renang = set()

# Input untuk klub Basket
jumlah_basket = int(input("Masukkan jumlah siswa yang mengikuti klub Basket: "))
for i in range(jumlah_basket):
    siswa = input(f"Masukkan nama siswa ke-{i+1} yang mengikuti klub Basket: ")
    klub_basket.add(siswa)

# Input untuk klub Renang
jumlah_renang = int(input("Masukkan jumlah siswa yang mengikuti klub Renang: "))
for i in range(jumlah_renang):
    siswa = input(f"Masukkan nama siswa ke-{i+1} yang mengikuti klub Renang: ")
    klub_renang.add(siswa)

# b. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("\nSiswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

# c. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_hanya_basket = klub_basket - klub_renang
siswa_hanya_renang = klub_renang - klub_basket
siswa_hanya_satu_klub = siswa_hanya_basket.union(siswa_hanya_renang)
print("\nSiswa yang hanya mengikuti satu klub:")
print(siswa_hanya_satu_klub)

# d. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
semua_siswa_unik = klub_basket.union(klub_renang)
print("\nSemua siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(semua_siswa_unik)

# e. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
jumlah_siswa_unik = len(semua_siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(jumlah_siswa_unik)