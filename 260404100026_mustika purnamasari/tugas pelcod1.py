#proses menghitung total belanja

#1.input
#(variabel)
#jumlah_buku = 3
#harga_buku = 15000
#jumlah_bulpen = 2
#harga_bulpen = 5000


#2.proses
#(menggunakan operasi aritmetika perkalian,penjumlahan,dan pengurangan)
#menghitung total harga buku(jumlah buku dikali harga buku)
#menghitung total harga bulpen(jumlah bulpen dikali harga bulpen )
#menghitung total belanja sebelum diskon(total harga buku ditambah total harga bulpen)
#(branching)
#menghitung total besarnya diskon(untuk bisa mendapatkan diskon 10%(0.10) maka total belanja sebelumnya harus diatas 50000,jika memenuhi syarat maka total belanja dikali 10%,jika tidak maka tidak akan dikalikan )
#menghitung total keseluruhan(total belanja dikurangi diskon)




jumlah_buku = 3
harga_buku = 15000

jumlah_pulpen = 2
harga_pulpen = 5000

total_buku = jumlah_buku * harga_buku
total_pulpen = jumlah_pulpen * harga_pulpen

total_belanja = total_buku + total_pulpen

if total_belanja >= 50000:
    diskon = total_belanja * 0.10
else:
    diskon = 0

total_bayar = total_belanja - diskon

print("Total harga buku   :", total_buku)
print("Total harga pulpen :", total_pulpen)
print("Total belanja      :", total_belanja)
print("Besarnya diskon    :", diskon)
print("Total yang dibayar :", total_bayar)