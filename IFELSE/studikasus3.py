print("Sistem perhitungan tarif parkir dan denda")

kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ").lower()
jam = int(input("Masukkan lama parkir (dalam jam): "))
karcis = input("Apakah anda memiliki karcis parkir? (ya/tidak): ").lower()

if kendaraan == "mobil":
    tarif = 5000
    lama = 3000
    jenis = "Mobil"
elif kendaraan == "motor":
    tarif = 1000
    lama = 1000
    jenis = "Motor"
else:
    print("Jenis kendaraan tidak valid.")
    

biaya_parkir = tarif + lama
denda = 0

if karcis == "ya":
    print(f"Anda memiliki karcis parkir untuk {jenis}.")
elif karcis == "tidak":
    denda = 50000
    print("Anda tidak memiliki karcis parkir.")
else:
    print("Input karcis tidak valid. Gunakan 'ya' atau 'tidak'.")
    

total_bayar = biaya_parkir + denda

print("\n====================================")
print("RINCIAN BIAYA PARKIR")
print("====================================")
print(f"Jenis kendaraan : {jenis}")
print(f"Lama parkir     : {jam} jam")
print(f"Biaya parkir    : Rp {biaya_parkir}")
print(f"Denda           : Rp {denda}")
print(f"Total bayar     : Rp {total_bayar}")