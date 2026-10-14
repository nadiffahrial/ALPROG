# 267006111157
# Nadif Ahmad Fahrial
# Kelas A
print("pengecekan tiket roller coaster")
umur = int(input("Masukkan umur anda: "))
tinggi = float(input("Masukkan tinggi badan anda (dalam cm): "))
harga = 100000

# kondisi if pertama
if umur >= 12:
    # nested if pertama
    if tinggi >= 130:
        print("Anda boleh naik roller coaster.")
        print(f"Harga tiket: Rp {harga}")
        member = input("Apakah anda memiliki member? (ya/tidak): ").lower()

        # nested if kedua
        if member == "ya":
            harga -= 10000
            print("anda mendapatkan diskon 10.000")

        print("total harga tiket: Rp", harga)
        uang = float(input("Masukkan uang anda: Rp "))

        # pengecekan pembayaran (operator perbandingan & aritmatika)
        if uang == harga:
            print("uang anda pas, transaksi berhasil.")
        elif uang > harga:
            print("Transaksi berhasil. Kembalian anda: Rp", uang - harga)
        else:
            print("Transaksi gagal. Uang anda kurang sebesar: Rp", harga - uang)
    else:
        print("tinggi anda tidak mencukupi (kurang dari 130 cm).")
else:
    print("Anda tidak boleh naik roller coaster karena umur tidak mencukupi.")