def insertion(array_list):
    n = len(array_list)
    print("##Data yang akan diurutkan", array_list)
    print("###Jumlah Data Array: ", n)
    print("####BuatPerulangan melalui seluruh array, dimulai dari indeks 1 (data ke-2)..dst")
    print("=================================================================================")
    for i in range(1, n):
        print("#####Simpan elemen saat ini yang akan dibandingkan")
        elemen_saat_ini = array_list[i]
        print("######Iterasi ke-", i, "Element Saat ini atau index ke", i, "adalah pada perulangan ke:",
              i, "nilai datanya adalah: ", elemen_saat_ini)
        print("#Pindahkan elemen-elemen yang lebih besar")
        j = i - 1
        while j >= 0 and elemen_saat_ini < array_list[j]:
            array_list[j + 1] = array_list[j]
            print("#Elemen yang lebih besar saat ini pada iterasi ke:",
                  i, "adalah", array_list[j + 1])
            j -= 1
        print("# Tempatkan elemen saat ini pada posisi yang benar")
        array_list[j + 1] = elemen_saat_ini
        print("#Posisi Yang benar Saat ini pada iterasi ke:",
              i, "untuk indek ke-", array_list.index(array_list[j + 1]), " adalah", array_list[j + 1])
        print("urutan Sementara", array_list)
        print("=================================================================================")


nilai = [4, 3, 2, 10, 12, 1, 5, 6]
# nilai = [39, 748, 256, 277, 975, 824, 70, 361, 564, 521, 237, 462, 746, 678, 76, 950, 275, 477, 456, 758, 33, 313, 652, 541, 166, 157, 865, 411, 557, 422, 968, 799, 856, 19, 27, 13, 633, 590, 272, 606, 70, 560, 690, 357, 546, 34, 801, 293, 722, 938,379, 89, 819, 586, 818, 996, 503, 695, 440, 145, 944, 216, 515, 953, 359, 71, 174, 578, 191, 976, 986, 337, 822, 826, 973, 666, 429, 692, 631, 700, 104, 113, 271, 42, 485, 757, 446, 82, 496, 457, 257, 170, 905, 179, 236, 462, 897, 810, 372, 345]
insertion(nilai)
print("Data setelah diurutkan", nilai)
