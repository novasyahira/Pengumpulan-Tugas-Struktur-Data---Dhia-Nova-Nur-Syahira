def manual_delete(arr, index):
    """
    Menghapus elemen pada indeks tertentu dengan menggeser elemen ke kiri.
    
    Parameters:
    arr (list): List yang akan dimodifikasi
    index (int): Indeks elemen yang akan dihapus
    """
    if index < 0 or index >= len(arr):
        print("Indeks tidak valid")
        return
    
    # Geser semua elemen dari indeks+1 ke kiri
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    
    # Hapus elemen terakhir dengan mengubah ukuran list
    arr.pop()


# Contoh penggunaan:
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print("Array awal:", data)
    
    manual_delete(data, 2)
    print("Setelah delete indeks 2:", data)
    
    manual_delete(data, 0)
    print("Setelah delete indeks 0:", data)
