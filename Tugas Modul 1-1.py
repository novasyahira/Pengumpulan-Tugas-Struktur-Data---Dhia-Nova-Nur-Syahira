# Demonstrasi Fenomena Aliasing pada List di Python

# Kasus 1: Assignment sederhana (Aliasing)
print("=== KASUS 1: ALIASING ===")
a = [1, 2, 3]
b = a  # b adalah alias dari a (menunjuk ke object yang sama)

print(f"List a sebelum perubahan: {a}")
print(f"List b sebelum perubahan: {b}")
print(f"ID a: {id(a)}, ID b: {id(b)}") # id () akan menghasilkan angka yang sama
print(f"Apakah a dan b menunjuk ke object yang sama? {a is b}\n") #

# Mengubah isi list a
a.append(4)
print(f"Setelah a.append(4):")
print(f"List a: {a}")
print(f"List b: {b}") # B ikut berubah karena 'B' adalah 'A'
print(f"List b ikut berubah! Ini adalah aliasing.\n")

# Kasus 2: Membuat copy (Bukan Aliasing)
print("=== KASUS 2: COPY (SHALLOW COPY) ===")
c = [1, 2, 3]
d = c.copy()  # d adalah copy dari c (object berbeda)

print(f"List c sebelum perubahan: {c}")
print(f"List d sebelum perubahan: {d}")
print(f"ID c: {id(c)}, ID d: {id(d)}") # id () akan menghasilkan angka yang berbeda
print(f"Apakah c dan d menunjuk ke object yang sama? {c is d}\n")

# Mengubah isi list c
c.append(4)
print(f"Setelah c.append(4):")
print(f"List c: {c}")
print(f"List d: {d}") # D tidak berubah karena dia adalah objek mandiri
print(f"List d tidak berubah. Ini adalah copy.\n")

# Penjelasan Memori
print("=== PENJELASAN MEMORI ===")
print("""
ALIASING (b = a):
- a dan b menunjuk ke LOKASI MEMORI yang SAMA
- Perubahan pada a akan terlihat pada b (dan sebaliknya)
- Menghemat memori, tapi berisiko jika ada perubahan tak terduga

COPY (d = c.copy()):
- c dan d menunjuk ke LOKASI MEMORI yang BERBEDA
- Perubahan pada c tidak mempengaruhi d
- Menggunakan lebih banyak memori, tapi lebih aman
""")
