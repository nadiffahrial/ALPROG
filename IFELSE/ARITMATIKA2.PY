# Variabel data
total_belanja = int(input("Masukkan total belanja: "))
status_member = "Silver"
punya_kupon = True

# Proses dengan Aritmatika, Perbandingan, dan Logika
if (total_belanja > 500000) and ((status_member == "Gold") or (punya_kupon == True)):
    diskon = total_belanja * 0.20  # Operasi aritmatika
    total_bayar = total_belanja - diskon
    print("Selamat! Anda mendapatkan diskon 20%.")
    print(f"Total yang harus dibayar: Rp {total_bayar}")
else:
    print("Maaf, Anda tidak memenuhi syarat diskon.")
    print(f"Total yang harus dibayar: Rp {total_belanja}")