def bubble_sort(arr):
    n = len(arr)

    # Melakukan iterasi sebanyak n kali (jumlah elemen dalam array)
    for i in range(n):
        # Perulangan dalam satu iterasi untuk memindahkan elemen terbesar ke ujung
        # Setelah iterasi ke-i, elemen terbesar akan ada di indeks n-i-1
        for j in range(0, n-i-1):
            # Bandingkan dua elemen berdekatan
            if arr[j] > arr[j+1]:
                # Jika elemen pertama lebih besar, maka tukar elemen tersebut
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Contoh penggunaan bubble_sort
angka = [64, 25, 12, 22, 11]
bubble_sort(angka)
print("Array setelah diurutkan:", angka)
