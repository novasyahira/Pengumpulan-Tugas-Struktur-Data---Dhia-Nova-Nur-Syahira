class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Bagian append
    def append(self, data):
        """Menambahkan node baru di akhir linked list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Bagian pencarian
    def search(self, key):
        """
        Mencari elemen dengan nilai 'key' dalam linked list.
        Mengembalikan True jika ditemukan, False jika tidak.
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Bagian pembalikan
    def reverse(self):
        """
        Membalik linked list
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Simpan node berikutnya
            current.next = prev       # Balik arah pointer
            prev = current            # Pindahkan prev ke current
            current = next_node       # Lanjut ke node berikutnya
        self.head = prev  # Kepala baru adalah prev

    # Bagian menampilkan isi list
    def print_list(self):
        """Menampilkan isi linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

# Contoh penggunaan dalam satu script
if __name__ == "__main__":
    ll = LinkedList()

    # Bagian 1: Menambahkan elemen
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Isi linked list:")
    ll.print_list()

    # Bagian 2: Mencari elemen
    print("Mencari 20:", ll.search(20))  # Output: True
    print("Mencari 50:", ll.search(50))  # Output: False

    # Bagian 3: Membalik linked list
    print("Sebelum dibalik:")
    ll.print_list()

    ll.reverse()

    print("Setelah dibalik:")
    ll.print_list()
