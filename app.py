#Hitung Luas Segitiga sederhana

def luas_segitiga():
    a = int(input("masukkan alas segitiga: "))
    t = int(input("Masukkan tinggi segitiga: "))
    luas = a * t / 2
    print("Luas segitiga adalah: ", luas)

luas_segitiga()

#Hitung Luas Persegi Panjang
def luas_persegi_panjang():
    p = int(input("Masukkan panjang persegi: "))
    l = int(input("Masukkan lebar persegi: "))
    luas = p * l\
    
    print("Luas persegi adalah: ", luas)

luas_persegi_panjang()

#Menghitung Teorema Pytagoras
def main():
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = (a**2 + b**2)**0.5
    print("Nilai c adalah: ", c)

main()