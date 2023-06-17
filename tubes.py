# menu yang akan dipesan (aziz)
def pilih_menu(menu):
    pesanan = []
    selesai = False

    while not selesai:
        print("\nMenu Makanan:")
        for i in range(len(menu)):
            item = menu[i][0]
            price = menu[i][1]
            print(f"{i+1}. {item} - Rp {price}")
        print("0. Selesai")

        pilihan = input("Masukkan nomor menu yang akan dipesan (0 untuk selesai): ")

        if pilihan == '0':
            selesai = True
        elif pilihan.isdigit() and int(pilihan) in range(1, len(menu) + 1):
            menu_index = int(pilihan) - 1
            pesanan.append(menu[menu_index])
            print("Menu telah ditambahkan ke dalam pesanan.")
        else:
            print("Menu tidak valid. Silakan pilih nomor menu yang tersedia.")

    if pesanan:
        print("\nPesanan Anda:")
        total_harga = 0
        for i, item in enumerate(pesanan, start=1):
            name = item[0]
            price = item[1]
            total_harga += price
            print(f"{i}. {name} - Rp {price}")
        print(f"Total Harga: Rp {total_harga}")
    else:
        print("Pesanan Anda kosong.")
    panggil(menu)
