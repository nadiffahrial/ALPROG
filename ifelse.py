nilai_siswa=int(input("Masukkan nilai siswa: "))
kehadiran=int(input("Masukkan persentase kehadiran siswa: "))
if nilai_siswa >= 80 and kehadiran >= 85:
    print("Selamat! Anda lulus dengan nilai yang baik.")
else:
    print("Maaf, Anda tidak lulus.")