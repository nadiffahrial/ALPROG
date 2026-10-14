rental_motor= float(70000)
print(f"Biaya rental motor: Rp {rental_motor}")
punya_ktp= bool(input("Apakah anda memiliki KTP? (ya/tidak): "))
lama_rental= int(input("Masukkan lama rental (dalam hari): "))
total_biaya= rental_motor * lama_rental
print(f"Total biaya rental: Rp {total_biaya}")
if lama_rental >=5 and punya_ktp:
    diskon= total_biaya * 0.10
    total_bayar= total_biaya - diskon
    print("Selamat! Anda mendapatkan diskon 10%.")
    print(f"Total yang harus dibayar: Rp {total_bayar}")
else:
    print("Maaf, Anda tidak memenuhi syarat diskon.")
    print(f"Total yang harus dibayar: Rp {total_biaya}")