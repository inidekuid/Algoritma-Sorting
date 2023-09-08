def selection_sort(array_list):
    n = len(array_list)
    print("##Data yang akan diurutkan", array_list)
    print("###Jumlah elemen Data: ", n)
    print("####Buat Perulangan melalui seluruh elemen, untuk cek nilai elemen terkecil")
    print("=================================================================================")
    for i in range(len(array_list)):
        # Temukan indeks elemen terkecil dalam bagian yang belum diurutkan
        min_index = i
        print("Bandingan Indeks ke-", min_index, "dengan seluruh elemen")
        for j in range(i + 1, len(array_list)):
            if array_list[j] < array_list[min_index]:
                min_index = j
                print("Pengecekan elemen terkecil pada index ke", j,
                      "elemen terkecilnya adalah:", array_list[min_index])

        # Tukar posisi elemen terkecil dengan elemen di indeks saat ini
        array_list[i], array_list[min_index] = array_list[min_index], array_list[i]
        print("tuker elemen dari indeks ke-", array_list.index(array_list[i]), " Yaitu ", array_list[min_index], "dengan indeks ", array_list.index(array_list[min_index]), "Yaitu ", array_list[i],
              "menjadi indeks ke-", array_list.index(array_list[i]), " Yaitu ", array_list[i], "dengan indeks ", array_list.index(array_list[min_index]), "Yaitu ", array_list[min_index])


# Contoh penggunaan selection_sort
angka = [64, 25, 12, 22, 11]
selection_sort(angka)
print("elemen setelah diurutkan:", angka)
