print("==============kalkulator patungan makanan==============")

nama=input("masukan nama anda:")
tagihan=int(input("masulan total tagihan:"))
persen = int(input("presentase tip/pajak:"))
jumlah_orang=int(input("jumlah orang yang ikut tagihan:"))

nominal_tip = tagihan * (persen/100)
total_tagihan = tagihan + nominal_tip
bayar_per_orang = total_tagihan / jumlah_orang

print("\n Halo!"+ nama)
print("Total Tagihan beserta tip adalah: Rp", total_tagihan)
print("Setiap orang harus membayar: Rp", bayar_per_orang)