import sys

# Integer sederhana
integer_simple = 42
size_integer = sys.getsizeof(integer_simple)

# List yang berisi satu integer
list_with_integer = [42]
size_list = sys.getsizeof(list_with_integer)

# Perbandingan
print(f"Ukuran integer sederhana: {size_integer} bytes")
print(f"Ukuran list dengan satu integer: {size_list} bytes")
print(f"Selisih: {size_list - size_integer} bytes")
print(f"List menggunakan {size_list / size_integer:.2f}x lebih besar dari integer")
