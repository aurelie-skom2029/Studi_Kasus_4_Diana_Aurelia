buku = {
    "Judul": "Laut Bercerita",
    "Penulis": "Leila S. Chudori",
    "Tahun Terbit": 2017
}

print("________________________________________")
print("\n    SISTEM PENGELOLAAN DATA BUKU")
print("________________________________________")

while True:
    print("\nMENU KELOLA DATA:")
    print("1. Lihat Data Buku")
    print("2. Tambah Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Keluar")

    pilihan = input("PILIH MENU (1-5): ")

    if pilihan == "1":
        print("_____________________")
        print("\n    DATA BUKU  ")
        print("_____________________")
        print(buku)

    elif pilihan == "2":
        print("_______________________________")
        print("\n   TAMBAH DATA PENERBIT ")
        print("_______________________________")
        buku["Penerbit"] = input("Masukkan Penerbit : ")

        print(buku)
        print(">>> DATA BERHASIL DITAMBAHKAN! <<<")

    elif pilihan == "3":
        print("___________________________")
        print("\n   UBAH DATA PENULIS ")
        print("___________________________")
        buku["Penulis"] = input("Masukkan Penulis Baru: ")

        print(buku)
        print(">>> DATA BERHASIL DIPERBARUI! <<<")

    elif pilihan == "4":
        del buku["Penerbit"]
        print(buku)

        print(">>> DATA BERHASIL DIHAPUS! <<<")

    elif pilihan == "5":
        print(">>> PROGRAM SELESAI <<<")
        break

    else:
        print("PILIHAN TIDAK VALID.")