angka1=int(input("Masukkan angka pertama : "))
operator=str(input("Masukkan operator (+, -, *, /,**, //, %): "))
angka2=int(input("Masukkan angka kedua : "))

hasil = {
    "+" : angka1 + angka2,
    "*" : angka1 * angka2,
    "/" : angka1 / angka2,
    "**" : angka1 ** angka2,
    "//" : angka1 // angka2,
    "%" : angka1 % angka2,
}
print ("hasil:", hasil[operator])
