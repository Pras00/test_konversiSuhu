class KonversiSuhu:

    # ----- CELCIUS -----
    # Fungsi konversi dari Celsius ke Reamur
    def celsius_ke_reamur(self, celsius):
        return celsius * 4/5

    # Fungsi konversi dari Celsius ke Fahrenheit
    def celsius_ke_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    # Fungsi konversi dari Celsius ke Kelvin
    def celsius_ke_kelvin(self, celsius):
        return celsius + 273

    # ----- REAMUR -----
    # Fungsi konversi dari Reamur ke Celsius
    def reamur_ke_celsius(self, reamur):
        return reamur * 5/4

    # Fungsi konversi dari Reamur ke Fahrenheit
    def reamur_ke_fahrenheit(self, reamur):
        return (reamur * 9/4) + 32

    # Fungsi konversi dari Reamur ke Kelvin
    def reamur_ke_kelvin(self, reamur):
        return (reamur * 5/4) + 273

    # ----- FAHRENHEIT -----
    # Fungsi konversi dari Fahrenheit ke Celsius
    def fahrenheit_ke_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    # Fungsi konversi dari Fahrenheit ke Kelvin
    def fahrenheit_ke_kelvin(self, fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273

    # Fungsi konversi dari Fahrenheit ke Reamur
    def fahrenheit_ke_reamur(self, fahrenheit):
        return (fahrenheit - 32) * 4/9

    # ----- KELVIN -----
    # Fungsi konversi dari Kelvin ke Celsius
    def kelvin_ke_celsius(self,kelvin):
        return kelvin - 273

    # Fungsi konversi dari Kelvin ke Fahrenheit
    def kelvin_ke_fahrenheit(self, kelvin):
        return (kelvin - 273) * 9/5 + 32

    # Fungsi konversi dari Kelvin ke Reamur
    def kelvin_ke_reamur(self, kelvin):
        return (kelvin - 273) * 4/5

def main():
    konversi = KonversiSuhu()

    print("Pilih satuan suhu awal:")
    print("1. Celsius")
    print("2. Reamur")
    print("3. Fahrenheit")
    print("4. Kelvin")
    pilihan_awal = int(input("Masukkan nomor pilihan: "))

    suhu_awal = float(input("Masukkan suhu: "))

    # Konversi Suhu
    print("Pilih satuan suhu konversi:")
    print("1. Celsius")
    print("2. Reamur")
    print("3. Fahrenheit")
    print("4. Kelvin")
    pilihan_konversi = int(input("Masukkan nomor pilihan: "))
    if pilihan_awal == 1:
        if pilihan_konversi == 1:
            hasil = suhu_awal
        elif pilihan_konversi == 2:
            hasil = konversi.celsius_ke_reamur(suhu_awal) 
        elif pilihan_konversi == 3:
            hasil = konversi.celsius_ke_fahrenheit(suhu_awal) 
        elif pilihan_konversi == 4:
            hasil = konversi.celsius_ke_kelvin(suhu_awal)
        else:
            hasil = "Pilihan konversi tidak valid"

    elif pilihan_awal == 2:  # Reamur
        if pilihan_konversi == 1:
            hasil = konversi.reamur_ke_celsius(suhu_awal)  
        elif pilihan_konversi == 2:
            hasil = suhu_awal  
        elif pilihan_konversi == 3:
            hasil = konversi.reamur_ke_fahrenheit(suhu_awal)  
        elif pilihan_konversi == 4:
            hasil = konversi.reamur_ke_kelvin(suhu_awal)
        else:
            hasil = "Pilihan konversi tidak valid"

    elif pilihan_awal == 3:  # Fahrenheit
        if pilihan_konversi == 1:
            hasil = konversi.fahrenheit_ke_celsius(suhu_awal) 
        elif pilihan_konversi == 2:
            hasil = konversi.fahrenheit_ke_reamur(suhu_awal) 
        elif pilihan_konversi == 3:
            hasil = suhu_awal 
        elif pilihan_konversi == 4:
            hasil = konversi.fahrenheit_ke_kelvin(suhu_awal)  
        else:
            hasil = "Pilihan konversi tidak valid"

    elif pilihan_awal == 4:  # Kelvin
        if pilihan_konversi == 1:
            hasil = konversi.kelvin_ke_celsius(suhu_awal)
        elif pilihan_konversi == 2:
            hasil = konversi.kelvin_ke_reamur(suhu_awal) 
        elif pilihan_konversi == 3:
            hasil = konversi.kelvin_ke_fahrenheit(suhu_awal) 
        elif pilihan_konversi == 4:
            hasil = suhu_awal
        else:
            hasil = "Pilihan konversi tidak valid"
    else:
        hasil = "Pilihan suhu awal tidak valid"


    print(f"Hasil Konversi: {hasil}°")


if __name__ == "__main__":
    main()
