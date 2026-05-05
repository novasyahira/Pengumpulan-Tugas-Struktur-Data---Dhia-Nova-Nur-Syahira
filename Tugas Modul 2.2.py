def balik_string(kalimat):
    hasil = ""
    
    # Loop dari belakang ke depan
    for i in range(len(kalimat) - 1, -1, -1):
        hasil += kalimat[i]
    
    return hasil


# Contoh penggunaan
teks = "Belajar Python"
print("Hasil:", balik_string(teks))
