print("==============sistem cek belanja & status pembayaran==============")
nama = input("masukan nama anda:")
harga_satuan_barang = float(input("masukan harga satuan barang:"))
jumlah_barang = int(input("masukan jumlah barang:"))
uang_dibayar = float(input("masukan uang yang diberikan ke kasir:"))

total_harga = harga_satuan_barang * jumlah_barang
selisih_uang = uang_dibayar - total_harga

uang_cukup = uang_dibayar >= total_harga
uang_pas = uang_dibayar == total_harga
uang_kurang = uang_dibayar < total_harga
print ("\n=== ringkasan transaksi===")
print("\nNama Pembeli:", nama)
print("Total Harga:", total_harga)
print("Selisih Uang (kembalian/kekurangan):", selisih_uang)

print("=============status true/false====================")
print("Apakah uang yang dibayarkan cukup?", uang_cukup)
print("Apakah pembeli membayar uang pas?", uang_pas)
print("Apakah pembeli berhutang?", uang_kurang)