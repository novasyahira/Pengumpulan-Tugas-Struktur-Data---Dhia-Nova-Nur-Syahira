def balikkan_kalimat(kalimat):
    """
    Membalikkan sebuah kalimat tanpa menggunakan [::-1] atau .reverse()
    
    Args:
        kalimat (str): Kalimat yang akan dibalikkan
    
    Returns:
        str: Kalimat yang sudah dibalikkan
    """
    hasil = ""
    for i in range(len(kalimat) - 1, -1, -1):
        hasil += kalimat[i]
    return hasil


# Contoh penggunaan
if __name__ == "__main__":
    teks = "Struktur Data"
    print(f"Kalimat asli: {teks}")
    print(f"Kalimat terbalik: {balikkan_kalimat(teks)}")
